package us.codecraft.webmagic.processor.example;

import us.codecraft.webmagic.Page;
import us.codecraft.webmagic.ResultItems;
import us.codecraft.webmagic.Site;
import us.codecraft.webmagic.Spider;
import us.codecraft.webmagic.pipeline.FilePipeline;
import us.codecraft.webmagic.processor.PageProcessor;

/**
 * @author code4crafter@gmail.com <br>
 * @since 0.4.0
 */
public class BaiduBaikePageProcessor implements PageProcessor {

    private Site site = Site.me()//.setHttpProxy(new HttpHost("127.0.0.1",8888))
            .setRetryTimes(3).setSleepTime(1000).setUseGzip(true);

    @Override
    public void process(Page page) {
    	 page.putField("author", page.getUrl().toString());
      
        
         
        page.putField("name", page.getHtml().css("h2.title","text").toString());
        page.putField("description", page.getHtml().xpath("//div[@id='lemmaContent-0']//div[@class='para']/allText()"));
    }

    @Override
    public Site getSite() {
        return site;
    }

    public static void main(String[] args) {
        //single download
        Spider spider = Spider.create(new BaiduBaikePageProcessor()).thread(2).addPipeline(new FilePipeline("F:\\webmagic\\"));
        String urlTemplate = "http://webmagic.io/";
        ResultItems resultItems = spider.<ResultItems>get(String.format(urlTemplate));
        System.out.println(resultItems);

        //multidownload
//        List<String> list = new ArrayList<String>();
//        list.add(String.format(urlTemplate,"web"));
//        list.add(String.format(urlTemplate,"site"));
//        list.add(String.format(urlTemplate,"big data"));
//        list.add(String.format(urlTemplate,"google"));
//        List<ResultItems> resultItemses = spider.<ResultItems>getAll(list);
//        for (ResultItems resultItemse : resultItemses) {
//            System.out.println(resultItemse.getAll());
//        }
        spider.close();
    }
}
