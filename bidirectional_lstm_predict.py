from keras_malicious_url_detector.library.bidirectional_lstm import BidirectionalLstmEmbedPredictor
from keras_malicious_url_detector.library.utility.url_data_loader import load_url_data


def main():

    data_dir_path = './data'
    model_dir_path = './models'

    predictor = BidirectionalLstmEmbedPredictor()
    predictor.load_model(model_dir_path)

    url_data = load_url_data(data_dir_path)
    count = 0
    for url, label in zip(url_data['text'], url_data['label']):
        predicted_label = predictor.predict(url)
        print('input url is:---->',url)
        print('predicted: ' + str(predicted_label) + ' actual: ' + str(label))
        count += 1
        if count > 20:
            break


if __name__ == '__main__':
    main()
