import cv2
from Graph_Head import FROZEN_GRAPH_HEAD

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT_HEAD = 'models/HEAD_DETECTION_300x300_ssd_mobilenetv2.pb'

# List of the strings that is used to add correct label for each box.
# PATH_TO_LABELS = 'protos/face_label_map.pbtxt'

# label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
# categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
# category_index = label_map_util.create_category_index(categories)

source = 'test.mp4'
# source = 0
writeVideo_flag = False
output_filename = 'cctv_output.avi'


tDetector = FROZEN_GRAPH_HEAD(PATH_TO_CKPT_HEAD)
cap = cv2.VideoCapture(source)

if writeVideo_flag:
    w = int(cap.get(3))
    h = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, fourcc, 30, (w, h))

while True:
       
    #ret, image = cap.read()
    image = cv2.imread("Test/7.jpg")
    # if ret == 0:
    #     break

    im_height, im_width, im_channel = image.shape
    image = cv2.flip(image, 1)

    boxes, scores = tDetector.run(image,im_width,im_height)
    #print(boxes[0])
    # boxes = np.squeeze(boxes).ravel()
    # scores = np.squeeze(scores)

    # for score, box in zip(scores, boxes):
    #      #print(box)
    #      if score["confidence"] > 0.7:
    #         print(score['confidence'])
    #          # ymin, xmin, ymax, xmax = box
    #         left = int(box[1]*im_width)
    #         top = int(box[0]*im_height)
    #         right = int(box[3]*im_width)
    #         bottom = int(box[2]*im_height)

    #         box_width = right-left
    #         box_height = bottom-top

            #cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), int(round(im_height/150)), 8)
            #cv2.putText(image, 'score: {:.3f}%'.format(score), (left, top), 0, 5e-3 * 130, (255,0,0),2)

    # fps = 1 / (time.time() - t_start)
    # cv2.putText(image, "FPS: {:.2f}".format(fps), (10, 30), 0, 5e-3 * 130, (0,0,255), 2)
    cv2.imshow("HEAD DETECTION USING FROZEN GRAPH", image)

    if writeVideo_flag:
        out.write(image)

    k = cv2.waitKey(1) & 0xff
    if k == ord('q') or k == 27:
        break

if writeVideo_flag:
    out.release()

cap.release()

cv2.destroyAllWindows()
