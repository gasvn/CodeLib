%%��ȡһ���ļ������mat���͵�ͼƬ���ݣ�ת��Ϊ��һ�ָ�ʽ
img_dir='A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\SymPASCAL-SRN\SymPASCAL';
save_dir = 'A:\Papers\2017.11_CVPR2017_Hi-Fi Skeleton\Data\final-models\SRN_sklarge_PASCAL';
if exist(save_dir, 'dir') ~= 7
   mkdir(save_dir);
end

imgs = dir(fullfile(img_dir, '*.mat')); imgs = {imgs.name};
for i = 1 : length(imgs)
  [~, fn, ext] = fileparts(imgs{i});
  in = load(fullfile(img_dir, [fn '.mat']))
  im=in.sym;%��Ϊmat��ʱ������struct���ͣ�����Ҫ��������ȡ���������ֽ�ɶ��һ����Ҫ���������mat�ļ������ɶ
  imwrite(im, fullfile(save_dir, [fn, '.png']));
end
