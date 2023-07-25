from viewer.viewer import Viewer
import numpy as np
from dataset.kitti_dataset import KittiDetectionDataset

def kitti_viewer():
    root = r"C:\datasets\DAIR\DAIR_I\kitti_format_example\training"
    label_path = r"C:\datasets\DAIR\DAIR_I\kitti_format_example\training/label_2"
    dataset = KittiDetectionDataset(root,label_path)

    vi = Viewer(box_type="Kitti")
    vi.set_ob_color_map('gnuplot')

    for i in range(len(dataset)):     # 如果文件名不是连续的数字，在加载数据的时候会有问题, 后边的数据也会丢掉
        try:
            P2, V2C, points, image, labels, label_names = dataset[i]
        except FileNotFoundError as error_str:
            print(error_str)

        # 只显示车的框
        # mask = label_names=="Car"
        # labels = labels[mask]
        # label_names = label_names[mask]

        vi.add_points(points[:,:3],scatter_filed=points[:,2],color_map_name='viridis')
        vi.add_3D_boxes(labels,box_info=label_names)
        vi.add_3D_cars(labels, box_info=label_names)
        vi.add_image(image)
        vi.set_extrinsic_mat(V2C)
        vi.set_intrinsic_mat(P2)
        vi.show_2D()
        vi.show_3D()


if __name__ == '__main__':
    kitti_viewer()
