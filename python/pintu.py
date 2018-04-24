#coding:utf-8
from PIL import Image, ImageDraw, ImageFont,ImageFile
import numpy as np
import os
import cv2
from os.path import join, isdir
import shutil
# options
#======================================================================
ngroups = 8
H = 300 # height of every component image (pixel)
W = 4000 # width of synthesised image (pixel)
marginv = 40 # vertical margin (pixel)
# margin of generated picture
margin_top, margin_right, margin_bottom, margin_left = 20, 0, 10, 150
all_imgs = []
im_dir = '/media/gao/projects/fmeasure/sal/allresult/pintu/ECSSD/'
#im_dir = '/media/conan/DATA/Papers/2018.04_NIPS2018_Floss/examples'
subpaths = ["img", "gt", "amulet","famulet","dhs","fdhs","dss", "fdss"] # put img folders in under the im_dir
resname="F_cmp"
tmp_dir="tmp"
if not isdir(tmp_dir):
  os.mkdir(tmp_dir)
sortby="selfrules"
#["fmeasure","fmeasurediff","selfrules"]

targetsortcat = 3
basesortcat = 2
imgcat=0
gtcat=1
sortcat=3
#======================================================================
def fmeasure(pred,target):
  pred/=pred.max()
  target/=target.max()
  beta=0.5
  FLT_MIN=1e-16
  target = target > 0
  h, w,_ = target.shape
  assert pred.max() <= 1 and pred.min() >= 0, "pred.max = %f, pred.min = %f" % (pred.max(), pred.min())
  #####with thrs####
  # thrs=0.5
  # pred[pred>thrs]=1
  # pred[pred<=thrs]=0
  TP=np.sum(target * pred)
  H = beta * target.sum() + pred.sum()
  fmeasure = (1 + beta) * TP / (H + FLT_MIN)
  return fmeasure
def sortbyfmeasure(imgs,im_dir,subpaths,sortcat,gtcat=1):
  print("Sorting by fmeasure score of %s"%(subpaths[sortcat]))
  fmesure_img=dict()
  for idx, j in enumerate(imgs):
    gt = cv2.imread(join(im_dir, subpaths[gtcat], j[:-4]+'.png'))
    im = cv2.imread(join(im_dir, subpaths[sortcat], j[:-4]+'.png'))
    fmesure_img[j]=fmeasure(im,gt)
  fimgs=sorted(fmesure_img.items(), key=lambda e:e[1], reverse=True)
  for idx, j in enumerate(fimgs):
    imgs[idx]=j[0]
  return imgs

def sortbyfmeasurediff(imgs,im_dir,subpaths,targetsortcat,basesortcat,gtcat=1):
  print("Sorting by fmeasure diff score of %s and %s"%(subpaths[targetsortcat],subpaths[basesortcat]))
  fmesure_img=dict()
  for idx, j in enumerate(imgs):
    gt = cv2.imread(join(im_dir, subpaths[gtcat], j[:-4]+'.png'))
    targetim = cv2.imread(join(im_dir, subpaths[targetsortcat], j[:-4]+'.png'))
    baseim = cv2.imread(join(im_dir, subpaths[basesortcat], j[:-4]+'.png'))
    fmesure_img[j]=fmeasure(targetim,gt)-fmeasure(baseim,gt)
  fimgs=sorted(fmesure_img.items(), key=lambda e:e[1], reverse=True)
  for idx, j in enumerate(fimgs):
    imgs[idx]=j[0]
  return imgs

def pickbyselfrules(imgs,im_dir):
  ######This function can be modified based on your specific rules.#######
  print("Sorting/Picking by modified rules")
  rule_img=[]
  for idx, j in enumerate(imgs):
    gt = cv2.imread(join(im_dir, subpaths[gtcat], j[:-4]+'.png'))
    targetim1 = cv2.imread(join(im_dir, "famulet", j[:-4]+'.png'))
    baseim1 = cv2.imread(join(im_dir, "amulet", j[:-4]+'.png'))
    targetim2 = cv2.imread(join(im_dir, "fdhs", j[:-4]+'.png'))
    baseim2 = cv2.imread(join(im_dir, "dhs", j[:-4]+'.png'))
    targetim3 = cv2.imread(join(im_dir, "fdss", j[:-4]+'.png'))
    baseim3 = cv2.imread(join(im_dir, "dss", j[:-4]+'.png'))
    if fmeasure(targetim1,gt)>fmeasure(baseim1,gt) and fmeasure(targetim2,gt)>fmeasure(baseim2,gt) and fmeasure(targetim3,gt)>fmeasure(baseim3,gt):
      rule_img.append(j)
  print rule_img
  return rule_img

def savetopdf(picture,im_dir,resname,rows_in_page,margin_top=20, margin_right=0, margin_bottom=10, margin_left=150):
  # add margin
  picture = np.pad(picture, ((margin_top, margin_bottom), (margin_left, margin_right), (0, 0)), mode='constant',
  constant_values=255)
  picture = Image.fromarray(picture)
  # draw text on image
  font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
  draw = ImageDraw.Draw(picture)
  y = margin_top + H // 2
  x = 16
  for r in range(rows_in_page):
    draw.text((x, y), subpaths[0], (0,0,0), font=font)
    y = y + H - 1
    for i in range(1,len(subpaths)):
      draw.text((x, y), subpaths[i], (0,0,0), font=font)
      y = y + H 
    draw = ImageDraw.Draw(picture)
    y = y + marginv
  #for r in range(len(rows)):
    # draw.text((x, y), 'img', (0,0,0), font=font)
    # y = y + H - 1
    # draw.text((x, y), 'gt', (0,0,0), font=font)
    # y = y + H 
    # draw.text((x, y), 'dss', (0,0,0), font=font)
    # y = y + H  
    # draw.text((x, y), 'sobeldss', (0,0,0), font=font)
    # y = y + H  
    # draw = ImageDraw.Draw(picture)
    # y = y + marginv
  print(picture.size)
  picture.save(join(im_dir,resname+'.pdf'))



assert len(subpaths) == ngroups
imgs = [i for i in os.listdir(join(im_dir, subpaths[0]))]
imgs.sort()

if sortby=="fmeasure":
  resname+="_f"
  imgs = sortbyfmeasure(imgs,im_dir,subpaths,sortcat,gtcat)
if sortby=="fmeasurediff":
  resname+="_fdiff"
  imgs = sortbyfmeasurediff(imgs,im_dir,subpaths,targetsortcat,basesortcat,gtcat=1)
if sortby=="selfrules":
  imgs = pickbyselfrules(imgs,im_dir)
# prepare images
print("Preparing images...")
nimgs = len(imgs)
widths = np.zeros((nimgs,), dtype=np.int)
for i in range(ngroups):
  all_imgs.append([])
  if i == imgcat:
    suffix = '.jpg'
  else:
    suffix = '.png'
  for idx, j in enumerate(imgs):
    im = Image.open(join(im_dir, subpaths[i], j[:-4]+suffix))
    w, h = im.size
    r = np.float(H) / h
    w1 = np.int(w * r)
    widths[idx] = w1
    im = np.array(im.resize((w1, H)), dtype=np.uint8)
    if im.ndim!=3:
      im = np.array(im)
      im = im[:,:,np.newaxis]
      im = np.repeat(im, 3, 2)
    all_imgs[i].append(im)
print("Prepared %d images into %d groups." % (ngroups * nimgs, ngroups))


rows = [[]]
w1 = np.int(0)
row_id = 0
for idx, w in enumerate(widths):
  if w1 + w >= W:
    # next row
    rows.append([])
    w1 = w
    row_id = row_id + 1
    rows[row_id].append(dict({"id": idx, "width": w}))
  else:
    w1 += w
    rows[row_id].append(dict({"id": idx, "width": w}))
# draw the picture
#picture = np.ones((len(rows) * (H * ngroups + marginv), W, 3), dtype=np.uint8) * 255
ystart = 0
pages = 0
rows_in_page=3
picture = np.ones((rows_in_page * (H * ngroups + marginv), W, 3), dtype=np.uint8) * 255
for ridx, r in enumerate(rows):
  # row
  for g in range(ngroups):
    # group
    yend = ystart + H
    xstart = 0
    # calculate horizontal margin
    w2 = 0
    for c in r:
      w2 = w2 + c['width']
    marginh = (W - w2) // (len(r) - 1)
    for cidx, c in enumerate(r):
      # column
      w = c['width']
      idx = c['id']
      xend = xstart + w
      picture[ystart:yend, xstart:xend, :] = all_imgs[g][idx]
      xstart = xstart + w + marginh
    ystart = ystart + H
  ##### split pages ######
  if (ridx+1) %rows_in_page==0:
    print "Generate page",pages
    savetopdf(picture,tmp_dir,resname+'_'+str(pages),rows_in_page,margin_top=20, margin_right=0, margin_bottom=10, margin_left=150) # save image to pdf
    picture = np.ones((rows_in_page * (H * ngroups + marginv), W, 3), dtype=np.uint8) * 255 # clear the picture buffer
    pages+=1
    ystart = 0
  else:
    ystart = ystart + marginv
savetopdf(picture,tmp_dir,resname+'_'+str(pages+1),rows_in_page,margin_top=20, margin_right=0, margin_bottom=10, margin_left=150) # save image to pdf
############concat all pdf#########
from PyPDF2 import PdfFileReader,PdfFileWriter

def getFileName(filepath):
    file_list = []
    for root,dirs,files in os.walk(filepath):
        for filespath in files:
            # print(os.path.join(root,filespath))
            file_list.append(os.path.join(root,filespath))

    return file_list

def MergePDF(filepath,outfile):
    output=PdfFileWriter()
    outputPages=0
    pdf_fileName=getFileName(filepath)
    for each in pdf_fileName:
        # read pdf
        input = PdfFileReader(file(each, "rb"))
        # if pdf is Encrypted，decrype
        if input.isEncrypted == True:
            input.decrypt("map")
        # pages numbers
        pageCount = input.getNumPages()
        outputPages += pageCount
        #print pageCount
        # put pages into output
        for iPage in range(0, pageCount):
            output.addPage(input.getPage(iPage))
    print "All Pages Number:"+str(outputPages)
    # write pdf
    outputStream=file(outfile,"wb")
    output.write(outputStream)
    outputStream.close()
    print "finished"

MergePDF(tmp_dir,join(im_dir,resname+'.pdf'))
shutil.rmtree(tmp_dir)

