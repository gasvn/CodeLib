%处理特定后缀名字的文件
%path:需要处理的文件夹路径，注意最后加上“\”，否则读不到文件
%suffix:特定的后缀名
function fileProcess(path,suffix)
files = dir([path,'*.',suffix]);
len = length(files);
for i = 1:len
    filePath = [path,files(i).name]; %得到文件路径
    %copyfile(filePath, 'sk_mat'); 把文件复制到sk_mat文件夹
    %movefile(filePath, '1');      % 把11.txt剪切到文件夹1中  
    %文件处理部分
end