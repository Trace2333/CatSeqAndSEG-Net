import argparse


class ArgsParse():
    pass


def get_parameter():
    parser = argparse.ArgumentParser(description="训练参数传递器")
    parser.add_argument("--train_file", help="填入运行的文件", type=str)
    parser.add_argument("--device", help="cuda or cpu", type=str)
    parser.add_argument("--seed", default=42, help="随机数种子", type=int)
    parser.add_argument("--batch_size", default=32, help="批次数", type=int)
    parser.add_argument("--input_size", default=300, help="输入的维度大小", type=int)
    parser.add_argument("--hidden_size1", default=300, help="第一个RNN隐藏层大小", type=int)
    parser.add_argument("--hidden_size2", default=300, help="第二个RNN隐藏层大小", type=int)
    parser.add_argument("--epochs", default=1, help="训练轮数", type=int)
    parser.add_argument("--lr", default=1e-3, help="学习率", type=float)
    parser.add_argument("--evaluation_epochs", default=1, help="评估的轮数，多次评估可以取平均值", type=int)
    parser.add_argument("--optim", default="Adam", help="优化器种类", type=str)
    parser.add_argument("--loss_fun", default="CrossEntropyLoss", help="损失函数", type=str)
    parser.add_argument("--project", help="记录的项目名", type=str)
    return parser.parse_args()

