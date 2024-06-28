# import cv2
# import numpy as np

# img = cv2.imread('./WechatIMG6321.jpg')

# # data=2*np.ones([200,200,3],np.uint8)
# data = 3 * np.ones(img.shape, np.uint8) 

# result1=cv2.add(img,data)

# result2=cv2.subtract(img,data)

# result3=cv2.multiply(img,data)

# result4=cv2.divide(img,data)

# cv2.imshow('img', img)
# cv2.imshow('result1', result1)
# cv2.imshow('result2', result2)
# cv2.imshow('result3', result3)
# cv2.imshow('result4', result4)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2
import numpy as np

def display_results_in_one_window(img, result1, result2, result3, result4):
    # 计算每张图片的高度和宽度
    height, width = img.shape[:2]
    
    # 创建一个新的空白画布，用于存放所有结果
    combined_img = np.zeros((height * 3, width * 2, 3), dtype=np.uint8) if len(img.shape) == 3 else np.zeros((height * 3, width * 2), dtype=np.uint8)
    
    # 将原图和四个处理结果分别放置到大图上
    combined_img[0:height, 0:width] = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) if len(img.shape) == 2 else img  # 如果是灰度图，转为三通道
    combined_img[height:2*height, 0:width] = result1
    combined_img[0:height, width:2*width] = result2
    combined_img[height:2*height, width:2*width] = result3
    combined_img[2*height:3*height, 0:width] = result4
    
    return combined_img

img=cv2.imread('./WechatIMG6321.jpg',cv2.IMREAD_GRAYSCALE)  # 读取灰度图
# img = cv2.imread('./WechatIMG6321.jpg', cv2.IMREAD_COLOR)  # 确保以彩色模式读取，以便与后续操作兼容

data = 3 * np.ones(img.shape, np.uint8)

result1=cv2.add(img,data)
result2=cv2.subtract(img,data)
result3=cv2.multiply(img,data)
result4=cv2.divide(img,data)

combined_results = display_results_in_one_window(img, result1, result2, result3, result4)

cv2.imshow('Combined Results', combined_results)
cv2.waitKey(0)
cv2.destroyAllWindows()