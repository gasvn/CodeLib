%�����ض���׺���ֵ��ļ�
%path:��Ҫ������ļ���·����ע�������ϡ�\��������������ļ�
%suffix:�ض��ĺ�׺��
function fileProcess(path,suffix)
files = dir([path,'*.',suffix]);
len = length(files);
for i = 1:len
    filePath = [path,files(i).name]; %�õ��ļ�·��
    %copyfile(filePath, 'sk_mat'); ���ļ����Ƶ�sk_mat�ļ���
    %movefile(filePath, '1');      % ��11.txt���е��ļ���1��  
    %�ļ�������
end