#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
from pathlib2 import Path
from io import open  # 新增导入

def generate_splits(data_dir, output_dir):
    """Generate dataset split files from directory structure"""
    splits = {
        'train': ('pages_train_jpg', 'trainset.txt'),
        'test': ('pages_test_jpg', 'testset.txt'),
        'devel': ('pages_devel_jpg', 'validationset_devel.txt')
    }

    data_path = Path(data_dir)
    
    for split_name, (dir_suffix, filename) in splits.items():
        split_dir = data_path / dir_suffix
        if not split_dir.exists():
            raise ValueError("Dataset directory missing: {0}".format(split_dir))

        file_ids = [f.stem for f in split_dir.glob("*.jpg")]
        
        output_path = Path(output_dir) / filename
        with output_path.open('w', encoding='utf-8') as f:  # 修改处
            f.write(u"\n".join(file_ids))  # 添加unicode前缀
        
        print("Generated {0} split file: {1}".format(split_name, output_path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate ICLEF dataset split files')
    parser.add_argument('--data-dir', type=str, required=True,
                        help='Root directory containing dataset folders')
    parser.add_argument('--output-dir', type=str, default="datasets/iclef",
                        help='Output directory for split files')
    args = parser.parse_args()

    generate_splits(args.data_dir, args.output_dir)