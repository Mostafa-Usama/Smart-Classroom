import time
import numpy as np
import tensorflow as tf
import cv2


class FROZEN_GRAPH_HEAD():
    def __init__(self, PATH_TO_CKPT):
        self.inference_list = []
        self.count = 0

        self.detection_graph = tf.Graph()
        with self.detection_graph.as_default():
            od_graph_def = tf.compat.v1.GraphDef()
            with tf.compat.v1.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

        with self.detection_graph.as_default():
            config = tf.compat.v1.ConfigProto()
            config.gpu_options.allow_growth = True
            self.sess = tf.compat.v1.Session(graph=self.detection_graph, config=config)
            self.windowNotSet = True

    def draw_bounding_box(self, image, scores, boxes, classes, im_width, im_height):
        boxes = np.squeeze(boxes)
        scores = np.squeeze(scores)
        classes = np.squeeze(classes).astype(np.int32)

        heads = list()
        idx = 1
        r = 0
        l = 0 

        for score, box, name in zip(scores, boxes, classes):
            if name == 1 and score > 0.5:
                #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3) #draw rectangle on the faces (image,top left point,bottom right point, color, thickness)
               
                # ymin, xmin, ymax, xmax = box
                left = int((box[1])*im_width)
                top = int((box[0])*im_height)
                right = int((box[3])*im_width)
                bottom = int((box[2])*im_height)

                cropped_head = np.array(image[top:bottom, left:right])

                
                width = right - left
                height = bottom - top
                bottom_mid = (left + int(width / 2), top + height)
                confidence = score
                if (left + (left + width))/2 >= im_width/2:
                    r +=1
                else:
                    l +=1

                mydict = {
                    "head_id": idx,
                    "width": width,
                    "height": height,
                    "cropped":cropped_head,
                    "left": left,
                    "right": right,
                    "top": top,
                    "bottom": bottom,
                    "confidence": confidence,
                    "label": None,
                    "bottom_mid": bottom_mid,
                    "model_type": 'FROZEN_GRAPH'
                    }
                heads.append(mydict)
                idx += 1
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2, 8)
                cv2.line(image, (im_width//2, 0), (im_width//2, im_height), (0, 255, 0), 2)

        return image, heads, r, l


    def run(self, image, im_width, im_height):
        """image: bgr image
        return (boxes, scores, classes, num_detections)
        """
        image_np = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # the array based representation of the image will be used later in order to prepare the
        # result image with boxes and labels on it.
        # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
        image_np_expanded = np.expand_dims(image_np, axis=0)
        image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
        # Actual detection.
        start_time = time.time()
        (boxes, scores, classes, num_detections) = self.sess.run(
            [boxes, scores, classes, num_detections],
            feed_dict={image_tensor: image_np_expanded})
        elapsed_time = time.time() - start_time
        self.inference_list.append(elapsed_time)
        self.count = self.count + 1

        # Draw bounding boxes on the image
        image, heads, r, l = self.draw_bounding_box(image, scores, boxes, classes, im_width, im_height)

        return image, heads, r, l