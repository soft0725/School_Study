import cv2

image = cv2.imread('./data/img.png')

# 순서: image, text, 첫시점, 폰트, 폰트 크기, 글 색깔, 글 굵기
cv2.putText(image, "Opencv", (600, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

cv2.imshow('text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()