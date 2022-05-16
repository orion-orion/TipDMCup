'''
Descripttion: 这个文件是写论文绘制ROC曲线用的
Version: 1.0
Author: ZhangHongYu
Date: 2021-02-27 11:20:37
LastEditors: ZhangHongYu
LastEditTime: 2022-05-16 15:17:48
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
# plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）
if __name__ == '__main__':
    data = pd.read_csv('data/roc_data.csv')
    list_y = [ data.iloc[:, i*2+1].tolist() for i in range(6) ]
    list_y.append(data.iloc[:, 11].tolist())
    list_x = [ data.iloc[:, i*2].tolist() for i in range(6) ]
    list_x.append(data.iloc[:, 10].tolist())
    plt.figure()
    colors = ['red', 'lightblue', 'yellowgreen', 'black', 'green', 'pink', 'orange']
    labels = ['stacking', 'xgb', 'rf', 'et', 'dt', 'knn', 'lr']
    AUCs = [0.8332, 0.8250, 0.8220, 0.8121, 0.8118, 0.8106, 0.8057]
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    for i in range(7):
        plt.plot(list_x[i], list_y[i], color = colors[i], label='AUC '+labels[i]+' = '+ str(AUCs[i]))
        plt.legend()
    plt.legend(loc='lower right')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC')

    plt.plot(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000), linestyle='--')
    plt.savefig('ROC.png')
