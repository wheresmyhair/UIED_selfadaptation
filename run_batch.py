import os
from tqdm import tqdm

import detect_compo.ip_region_proposal as ip
import input_processing.img_preprocessing as img_preprocessing
import input_processing.files_op as files_op


if __name__ == '__main__':
    # initialization
    input_img_root = "./data/local/input"
    output_root = "./data/local/output"

    input_imgs = files_op.get_files(input_img_root, combine=True)

    key_params = {'min-grad':10, 'ffl-block':5, 'min-ele-area':50,
                'merge-contained-ele':True, 'merge-line-to-paragraph':False, 'remove-bar':True}


    is_ip = True
    is_clf = False
    is_ocr = True
    is_merge = True

    # Load deep learning models in advance
    compo_classifier = None
    if is_ip and is_clf:
        compo_classifier = {}
        from cnn.CNN import CNN
        # compo_classifier['Image'] = CNN('Image')
        compo_classifier['Elements'] = CNN('Elements')
        # compo_classifier['Noise'] = CNN('Noise')

    if is_ocr:
        import detect_text.text_detection as text
        ocr_model = text.preload_text_detection()

    os.makedirs(os.path.join(output_root, 'ocr'), exist_ok=True)
    os.makedirs(os.path.join(output_root, 'ip'), exist_ok=True)
    os.makedirs(os.path.join(output_root, 'merge'), exist_ok=True)
    # set the range of target inputs' indices
    for input_img in tqdm(input_imgs):
        file_name = os.path.split(input_img)[1].split('.')[0]
        resized_height = img_preprocessing.resize_height_by_longest_edge(input_img)

        if is_ocr:
            text.text_detection_preload_model(input_img, output_root, ocr_model, show=False)

        if is_ip:
            ip.compo_detection(input_img, output_root, key_params,  classifier=compo_classifier, resize_by_height=resized_height, show=False)

        if is_merge:
            import detect_merge.merge as merge
            compo_path = os.path.join(output_root, 'ip', str(file_name) + '.json')
            ocr_path = os.path.join(output_root, 'ocr', str(file_name) + '.json')
            merge.merge(input_img, compo_path, ocr_path, os.path.join(output_root, 'merge'),
                        is_remove_bar=key_params['remove-bar'], is_paragraph=key_params['merge-line-to-paragraph'], show=False)

