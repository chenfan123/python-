# 基于传入的数值（每批次的歌词条数），创建生成器，生成批次歌词
# 需求：基于文件，创建生成器，根据传入的每批次的歌词条数，生成歌词批次。
def dataset_loader(batch_size):
    """
    自定义的 歌词 批量生成器
    :param batch_size: 每批次的歌词条数
    :return: 生成器 每个元素都是一批次的数据
    """
    # 1.1 读取文件数据
    with open('data/lyrics.txt', 'r', encoding='utf-8') as f:
        # 一次读取所有航
        # 1.2 遍历所有行
        lines = [line.strip() for line in f.readlines()]
        # 1.3 遍历所有行，生成批次
        for i in range(0, len(lines), batch_size):
            # 1.4 切片获取一批次的数据
            batch = lines[i:i + batch_size]
            i = i + batch_size
            # 1.5 返回一批次的数据
            yield batch
        if i < len(lines):
            batch = lines[i:]
            yield batch
            
if __name__ == '__main__':
    g = dataset_loader(3)
    for batch in g:
        print(batch)
        