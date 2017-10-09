from scrapy.exceptions import DropItem
import os
import urllib
import settings

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        # for word in self.words_to_filter:
        #     if word in item['description'].lower():
        #         raise DropItem("Contains forbidden word: %s" % word)
        # else:
        dir_path = '%s/%s'%(settings.IMAGES_STORE,spider.name)
        print 'dir_path',dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['url']:
            list_name = image_url.split('/')
            file_name = list_name[len(list_name)-1]
            # print 'filename',file_name
            file_path = '%s/%s'%(dir_path,file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                conn = urllib.urlopen(image_url)
                file_writer.write(conn.read())
            file_writer.close()
        return item
