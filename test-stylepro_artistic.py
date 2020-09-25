import paddlehub as hub
import cv2


def style():
    stylepro_artistic = hub.Module(name="stylepro_artistic")
    result = stylepro_artistic.style_transfer(
        images=[{
            'content': cv2.imread('2.jpg'),
            'styles': [cv2.imread('1.jpg')],
        }], output_dir='static/images/stylepro_artistic', visualization=True, use_gpu=False)
    filepath = result[0]["save_path"]
    print('filepath: %s' % filepath)


if __name__ == '__main__':
    style()
