%%读取一个文件夹里的mat类型的图片数据，转换为另一种格式
img_dir='A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\SymPASCAL-SRN\SymPASCAL';
save_dir = 'A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\SRN_sklarge_PASCAL';
if exist(save_dir, 'dir') ~= 7
   mkdir(save_dir);
end

imgs = dir(fullfile(img_dir, '*.mat')); imgs = {imgs.name};
for i = 1 : length(imgs)
  [~, fn, ext] = fileparts(imgs{i});
  in = load(fullfile(img_dir, [fn '.mat']))
  im=in.sym;%因为mat有时候寸的是struct类型，所以要从里面提取出来，名字叫啥不一定，要看下载入的mat文件里面叫啥
  imwrite(im, fullfile(save_dir, [fn, '.png']));
end
