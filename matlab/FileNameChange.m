%%��ȡһ���ļ������ĳ�ָ�ʽ��ͼƬ��ת��Ϊ��һ�����֣������ļ������ȸ�Ƚϼ�)
% img_dir='A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\fsds_WH-SYMMAX1';
% save_dir = 'A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\fsds_WH-SYMMAX\data';

img_dir='A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\SRN_WH-SYMMAX1';
save_dir = 'A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\SRN_WH-SYMMAX\data';
if exist(save_dir, 'dir') ~= 7
   mkdir(save_dir);
end
    
imgs = dir(fullfile(img_dir, '*.png')); imgs = {imgs.name};
for i = 1 : length(imgs)
  [~, fn, ext] = fileparts(imgs{i});
  if length(fn)<15
    im = imread(fullfile(img_dir, [fn,'.png']));
    fn=fn(1:8);%��ȡ��������
    imwrite(im, fullfile(save_dir, [fn, '.png']));
  end
end
