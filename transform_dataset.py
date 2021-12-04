import json
with open("./datasets/coco_caption/test.label.tsv", 'r') as f:
    lines = f.readlines()
ids = []
for line in lines:
    ids.append(line.split('\t')[0])
print(ids)
with open("./datasets/coco_caption/test_caption.json", 'r') as f:
    captions = json.load(f)
print(captions)
res = []
for id in ids[0:100]:
    for dict in captions:
        if dict['image_id'] == id:
            res.append(dict)
            break
print(res)
with open("test_caption_overfit.json", 'w') as f:
    json.dump(res, f)