import pandas as pd
import json
import os
import matplotlib.pyplot as plt

original_path = os.getcwd() + "\\files\\deviation.json"


class DrawPlot:

    def __init__(self):
        self.created_directory_path = "plots"
        self.path = os.getcwd() + "\\plots"
        self.direction_list = []

    def draw_plots(self, file_path):
        with open(file_path) as f:
            df = pd.DataFrame(data=json.load(f))
        try:
            os.mkdir(self.created_directory_path)
        except OSError:
            print("Directory already exists")
        else:
            print("Successfully created the directory")

        df['check'] = (df['gt_corners'] == df['rb_corners'])
        check_df = (df['check'].value_counts())

        new = check_df.plot.pie(figsize=(5, 5), colors=['green', 'red'], ylabel="")
        new.set_xlabel("Количество совпадающих значений к не совпадающим")
        plt.savefig('{valid_path}\\valid.png'.format(valid_path=self.path))
        self.direction_list.append("{path}\\valid.png".format(path=self.path))

        gt_df = (df['gt_corners'].value_counts())
        gt_df.plot.pie(ylabel='количество углов', figsize=(5, 5))
        plt.savefig('{amount_path}\\amount.png'.format(amount_path=self.path))
        self.direction_list.append("{path}\\amount.png".format(path=self.path))

        return self.direction_list


if __name__ == '__main__':
    new_plot = DrawPlot()
    path_list = new_plot.draw_plots(original_path)
    print(path_list)