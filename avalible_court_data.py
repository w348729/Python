import re
import csv
import requests
from tqdm import tqdm
import BeautifulSoup
from requests.exceptions import RequestException



venue_list = [{"venue_id":"331","name":"Ahmad Ibrahim Secondary School Field"},
              {"venue_id":"551","name":"Anchor Green Primary School Hall"},
              {"venue_id":"334","name":"Anderson Secondary School Field"},
              {"venue_id":"322","name":"Anderson Secondary School Hall"},
              {"venue_id":"867","name":"Ang Mo Kio Primary School Hall"},
              {"venue_id":"337","name":"Ang Mo Kio Secondary School Field"},
              {"venue_id":"460","name":"Ang Mo Kio Secondary School Hall"},
              {"venue_id":"949","name":"Anglican High School Hall"},
              {"venue_id":"445","name":"Bartley Secondary School Field"},
              {"venue_id":"930","name":"Bartley Secondary School Hall"},
              {"venue_id":"339","name":"Beatty Secondary School Field"},
              {"venue_id":"420","name":"Beatty Secondary School Hall"},
              {"venue_id":"341","name":"Bedok Green Secondary School Field"},
              {"venue_id":"343","name":"Bedok North Secondary School Field"},
              {"venue_id":"421","name":"Bedok North Secondary School Hall"},
              {"venue_id":"346","name":"Bedok South Secondary School Field"},
              {"venue_id":"323","name":"Bedok South Secondary School Hall"},
              {"venue_id":"348","name":"Bedok View Secondary School Field"},{"venue_id":"324","name":"Bedok View Secondary School Hall"},{"venue_id":"821","name":"Bendemeer Primary School Hall"},{"venue_id":"351","name":"Bendemeer Secondary School Field"},{"venue_id":"554","name":"Bendemeer Secondary School Hall"},{"venue_id":"292","name":"Bishan Sports Hall"},{"venue_id":"871","name":"Blangah Rise Primary School Hall"},{"venue_id":"356","name":"Boon Lay Secondary School Field"},{"venue_id":"822","name":"Boon Lay Secondary School Hall "},{"venue_id":"360","name":"Bowen Secondary School Field"},{"venue_id":"869","name":"Bowen Secondary School Hall"},{"venue_id":"363","name":"Broadrick Secondary School Field"},{"venue_id":"293","name":"Bukit Gombak Sports Hall"},{"venue_id":"367","name":"Bukit Merah Secondary School Field"},{"venue_id":"888","name":"Bukit Panjang Govt High School Field"},{"venue_id":"823","name":"Bukit Panjang Govt High School Hall "},{"venue_id":"879","name":"Bukit Panjang Primary School Hall"},{"venue_id":"415","name":"Bukit View Secondary School Field"},{"venue_id":"325","name":"Bukit View Secondary School Hall"},{"venue_id":"294","name":"Burghley Squash Centre"},{"venue_id":"150","name":"Burghley Tennis Centre"},{"venue_id":"877","name":"Canberra Primary School Hall"},{"venue_id":"370","name":"Canberra Secondary School Field"},{"venue_id":"919","name":"Canberra Secondary School Hall"},{"venue_id":"824","name":"Cantonment Primary School Hall"},{"venue_id":"933","name":"Casuarina Primary School Hall"},{"venue_id":"942","name":"CHIJ St Theresa Convent School Hall"},{"venue_id":"864","name":"CHIJ St. Joseph's Convent School Hall"},{"venue_id":"809","name":"Choa Chu Kang Conference Room"},{"venue_id":"382","name":"Choa Chu Kang Secondary School Field"},{"venue_id":"295","name":"Choa Chu Kang Sports Hall"},{"venue_id":"156","name":"Choa Chu Kang Street Soccer Court"},{"venue_id":"158","name":"Choa Chu Kang Tennis Centre"},{"venue_id":"564","name":"Clementi Primary School Hall"},{"venue_id":"296","name":"Clementi Sports Hall"},{"venue_id":"416","name":"Clementi Town Secondary School Field"},{"venue_id":"565","name":"Clementi Town Secondary School Hall"},{"venue_id":"388","name":"Commonwealth Secondary School Field"},{"venue_id":"566","name":"Commonwealth Secondary School Hall"},{"venue_id":"390","name":"Compassvale Secondary School Field"},{"venue_id":"957","name":"Compassvale Secondary School Hall"},{"venue_id":"918","name":"Concord Primary School Hall"},{"venue_id":"440","name":"Crescent Girls School Field"},{"venue_id":"555","name":"Crescent Girls Secondary School Hall"},{"venue_id":"627","name":"Crest Secondary School Field"},{"venue_id":"735","name":"Crest Secondary School Hall"},{"venue_id":"761","name":"Crest Secondary School Outdoor Basketball Court"},{"venue_id":"743","name":"Crest Secondary School Street Soccer Court"},{"venue_id":"393","name":"Damai Secondary School Field"},{"venue_id":"167","name":"Delta Hockey Pitch"},{"venue_id":"298","name":"Delta Sports Hall"},{"venue_id":"804","name":"Delta Sports Hall - Meeting Room"},{"venue_id":"397","name":"Deyi Secondary School Field"},{"venue_id":"852","name":"Dunman High School Field"},{"venue_id":"825","name":"Dunman High School Hall"},{"venue_id":"920","name":"Dunman Secondary School Field"},{"venue_id":"874","name":"East Spring Primary School Hall"},{"venue_id":"362","name":"East Spring Secondary School Field"},{"venue_id":"422","name":"East Spring Secondary School Hall"},{"venue_id":"365","name":"East View Secondary School Field"},{"venue_id":"423","name":"East View Secondary School Hall"},{"venue_id":"826","name":"Edgefield Secondary School Hall "},{"venue_id":"326","name":"Endeavour Primary School Hall"},{"venue_id":"952","name":"Fajar Secondary School Field"},{"venue_id":"953","name":"Fajar Secondary School Hall"},{"venue_id":"175","name":"Farrer Park Field"},{"venue_id":"300","name":"Farrer Park Tennis Centre"},{"venue_id":"916","name":"First Toa Payoh Primary School Hall"},{"venue_id":"378","name":"Former Chestnut Drive Secondary School Field"},{"venue_id":"567","name":"Frontier Primary School Hall"},{"venue_id":"375","name":"Fuchun Secondary School Field"},{"venue_id":"379","name":"Fuhua Secondary School Field"},{"venue_id":"424","name":"Fuhua Secondary School Hall"},{"venue_id":"854","name":"Gan Eng Seng Primary School Hall"},{"venue_id":"453","name":"Gan Eng Seng Secondary School Hall"},{"venue_id":"330","name":"Gongshang Primary School Hall"},{"venue_id":"328","name":"Greendale Primary School Hall"},{"venue_id":"417","name":"Greendale Secondary School Field"},{"venue_id":"923","name":"Greenridge Primary School Hall"},{"venue_id":"576","name":"Greenridge Secondary School Field"},{"venue_id":"559","name":"Greenridge Secondary School Hall"},{"venue_id":"347","name":"Greenview Secondary School Field"},{"venue_id":"860","name":"Greenwood Primary School Hall"},{"venue_id":"543","name":"Hai Sing Catholic School Field"},{"venue_id":"944","name":"Haig Girls' Primary School Hall"},{"venue_id":"895","name":"Heartbeat @ Bedok ActiveSG Sports Hall"},{"venue_id":"897","name":"Heartbeat @ Bedok ActiveSG Tennis Centre"},{"venue_id":"950","name":"Henry Park Primary School Hall"},{"venue_id":"948","name":"Hillgrove Secondary School Hall"},{"venue_id":"932","name":"Holy Innocents Secondary School Hall"},{"venue_id":"915","name":"Hong Kah Secondary School Field"},{"venue_id":"454","name":"Hong Kah Secondary School Hall"},{"venue_id":"803","name":"Hougang Meeting Room"},{"venue_id":"329","name":"Hougang Primary School Hall"},{"venue_id":"889","name":"Hougang Secondary School Field"},{"venue_id":"827","name":"Hougang Secondary School Hall "},{"venue_id":"301","name":"Hougang Sports Hall"},{"venue_id":"353","name":"Hua Yi Secondary School Field"},{"venue_id":"332","name":"Hua Yi Secondary School Hall"},{"venue_id":"333","name":"Innova Primary School Hall"},{"venue_id":"811","name":"Jalan Besar Conference Room"},{"venue_id":"457","name":"Junyuan Primary School Hall"},{"venue_id":"357","name":"Junyuan Secondary School Field"},{"venue_id":"858","name":"Junyuan Secondary School Hall"},{"venue_id":"808","name":"Jurong East Conference Room"},{"venue_id":"195","name":"Jurong East Gateball Court"},{"venue_id":"197","name":"Jurong East Petanque Courts"},{"venue_id":"302","name":"Jurong East Sports Hall"},{"venue_id":"437","name":"Jurong East Sports Hall Table Tennis Area"},{"venue_id":"455","name":"Jurong Secondary School Hall"},{"venue_id":"807","name":"Jurong West Conference Room"},{"venue_id":"806","name":"Jurong West Meeting Room"},{"venue_id":"935","name":"Jurong West Primary School Hall"},{"venue_id":"361","name":"Jurong West Secondary School Field"},{"venue_id":"425","name":"Jurong West Secondary School Hall"},{"venue_id":"304","name":"Jurong West Sports Hall"},{"venue_id":"204","name":"Jurong West Tennis Centre"},{"venue_id":"921","name":"Jurongville Secondary School Field"},{"venue_id":"828","name":"Jurongville Secondary School Hall"},{"venue_id":"364","name":"Juying Secondary School Field"},{"venue_id":"829","name":"Juying Secondary School Hall "},{"venue_id":"583","name":"Kallang Lawn Bowl"},{"venue_id":"208","name":"Kallang Netball Centre"},{"venue_id":"211","name":"Kallang Squash Centre"},{"venue_id":"305","name":"Kallang Tennis Centre"},{"venue_id":"885","name":"Keming Primary School Hall"},{"venue_id":"369","name":"Kent Ridge Secondary School Field"},{"venue_id":"452","name":"Kent Ridge Secondary School Hall"},{"venue_id":"862","name":"Lakeside Primary School Hall"},{"venue_id":"955","name":"Lianhua Primary School Hall"},{"venue_id":"381","name":"Marsiling Secondary School Field"},{"venue_id":"384","name":"Mayflower Secondary School Field"},{"venue_id":"881","name":"Mayflower Secondary School Hall"},{"venue_id":"414","name":"Meridian Junior College Field"},{"venue_id":"934","name":"Meridian Primary School Hall"},{"venue_id":"418","name":"Meridian Secondary School Field"},{"venue_id":"556","name":"Meridian Secondary School Hall"},{"venue_id":"318","name":"MOE (Evans) Sports Hall"},{"venue_id":"250","name":"MOE (Evans) Squash Centre"},{"venue_id":"253","name":"MOE (Evans) Tennis Centre"},{"venue_id":"248","name":"MOE Evans Hockey Pitch"},{"venue_id":"249","name":"MOE Evans Outdoor Facilities"},{"venue_id":"391","name":"Nan Hua High School Field"},{"venue_id":"426","name":"Nan Hua High School Hall"},{"venue_id":"441","name":"Naval Base Secondary School Field"},{"venue_id":"446","name":"Naval Base Secondary School Hall"},{"venue_id":"856","name":"New Town Primary School Hall"},{"venue_id":"220","name":"North View Secondary School Field"},{"venue_id":"883","name":"North Vista Primary School Hall"},{"venue_id":"395","name":"North Vista Secondary School Field"},{"venue_id":"830","name":"North Vista Secondary School Hall"},{"venue_id":"400","name":"Northbrooks Secondary School Field"},{"venue_id":"751","name":"Northland Primary School Hall"},{"venue_id":"560","name":"Northland Secondary School Hall"},{"venue_id":"831","name":"Northoaks Primary School Hall"},{"venue_id":"960","name":"NUS University Sports Centre"},{"venue_id":"961","name":"NUS University Sports Centre Tennis Courts"},{"venue_id":"959","name":"NUS University Town, Stephen Riady Centre, Hall 1"},{"venue_id":"884","name":"Oasis Primary School Hall"},{"venue_id":"399","name":"Orchid Park Secondary School Field"},{"venue_id":"850","name":"Our Tampines Hub - Community Auditorium"},{"venue_id":"310","name":"Our Tampines Hub - Team Sports Hall"},{"venue_id":"832","name":"Palm View Primary School Hall"},{"venue_id":"540","name":"Pasir Ris 5 a Side Soccer"},{"venue_id":"402","name":"Pasir Ris Crest Secondary School Field"},{"venue_id":"459","name":"Pasir Ris Crest Secondary School Hall"},{"venue_id":"406","name":"Pasir Ris Secondary School Field"},{"venue_id":"338","name":"Pasir Ris Secondary School Hall"},{"venue_id":"542","name":"Pasir Ris Sports Hall"},{"venue_id":"586","name":"Pasir Ris Sports Hall Table Tennis Area"},{"venue_id":"539","name":"Pasir Ris Tennis Centre"},{"venue_id":"409","name":"Pei Hwa Secondary School Field"},{"venue_id":"447","name":"Peicai Secondary School Hall"},{"venue_id":"553","name":"Peirce Secondary School Hall"},{"venue_id":"413","name":"Ping Yi Secondary School Field"},{"venue_id":"427","name":"Ping Yi Secondary School Hall"},{"venue_id":"557","name":"Poi Ching School Hall"},{"venue_id":"938","name":"Princess Elizabeth Primary School Hall"},{"venue_id":"408","name":"Punggol Secondary School Field"},{"venue_id":"458","name":"Punggol Secondary School Hall"},{"venue_id":"947","name":"Punggol View Primary School Hall"},{"venue_id":"887","name":"Qihua Primary School Hall"},{"venue_id":"833","name":"Queenstown Primary School Hall "},{"venue_id":"442","name":"Queenstown Secondary School Field"},{"venue_id":"405","name":"Queensway Secondary School Field"},{"venue_id":"430","name":"Queensway Secondary School Hall"},{"venue_id":"834","name":"Radin Mas Primary School Hall"},{"venue_id":"943","name":"Raffles Girls' Primary School Hall"},{"venue_id":"403","name":"Regent Secondary School Field"},{"venue_id":"396","name":"Riverside Secondary School Field"},{"venue_id":"431","name":"Riverside Secondary School Hall"},{"venue_id":"835","name":"Sembawang Primary School Hall"},{"venue_id":"392","name":"Sembawang Secondary School Field"},{"venue_id":"340","name":"Sembawang Secondary School Hall"},{"venue_id":"928","name":"Seng Kang Primary School Hall"},{"venue_id":"929","name":"Seng Kang Secondary School Hall"},{"venue_id":"813","name":"Sengkang Conference Room"},{"venue_id":"866","name":"Sengkang Green Primary School Hall"},{"venue_id":"240","name":"Sengkang Hockey Pitch"},{"venue_id":"389","name":"Sengkang Secondary School Field"},{"venue_id":"308","name":"Sengkang Sports Hall"},{"venue_id":"443","name":"Serangoon Garden Secondary School Field"},{"venue_id":"449","name":"Serangoon Garden Secondary School Hall"},{"venue_id":"385","name":"Serangoon Secondary School Field"},{"venue_id":"244","name":"Serangoon Swimming Complex"},{"venue_id":"924","name":"Shuqun Primary School Hall"},{"venue_id":"578","name":"Shuqun Secondary School Field"},{"venue_id":"451","name":"Shuqun Secondary School Hall"},{"venue_id":"349","name":"Si Ling Secondary School Field"},{"venue_id":"880","name":"South View Primary School Hall"},{"venue_id":"599","name":"Spectra School Hall"},{"venue_id":"892","name":"Spectra Secondary School Field"},{"venue_id":"355","name":"Springfield Secondary School Field"},{"venue_id":"859","name":"Springfield Secondary School Hall"},{"venue_id":"577","name":"St Gabriel's Secondary School Field"},{"venue_id":"937","name":"St Patrick's School Hall"},{"venue_id":"255","name":"St Wilfred Field"},{"venue_id":"309","name":"St Wilfred Squash Centre"},{"venue_id":"256","name":"St Wilfred Tennis Centre"},{"venue_id":"863","name":"St. Anthony's Primary School Hall"},{"venue_id":"562","name":"St. Gabriel'S Secondary School Hall"},{"venue_id":"861","name":"Swiss Cottage Secondary School Hall"},{"venue_id":"359","name":"Tampines Secondary School Field"},{"venue_id":"366","name":"Tanglin Secondary School Field"},{"venue_id":"373","name":"Tanjong Katong Secondary School Field"},{"venue_id":"857","name":"Tanjong Katong Secondary School Hall"},{"venue_id":"917","name":"Tao Nan Primary School Hall"},{"venue_id":"945","name":"Teck Whye Primary School Hall"},{"venue_id":"872","name":"Temasek Primary School Hall"},{"venue_id":"873","name":"Temasek Secondary School Hall"},{"venue_id":"812","name":"Toa Payoh conference Room"},{"venue_id":"266","name":"Toa Payoh Petanque Courts"},{"venue_id":"311","name":"Toa Payoh Sports Hall"},{"venue_id":"882","name":"Townsville Primary School Hall"},{"venue_id":"433","name":"Unity Primary School Hall"},{"venue_id":"575","name":"Unity Secondary School Field"},{"venue_id":"342","name":"Unity Secondary School Hall"},{"venue_id":"865","name":"Waterway Primary School Hall"},{"venue_id":"394","name":"West Spring Secondary School Field"},{"venue_id":"432","name":"West Spring Secondary School Hall"},{"venue_id":"398","name":"Westwood Secondary School Field"},{"venue_id":"936","name":"Westwood Secondary School Hall"},{"venue_id":"401","name":"Woodgrove Secondary School Field"},{"venue_id":"878","name":"Woodlands Ring Primary School Hall"},{"venue_id":"404","name":"Woodlands Ring Secondary School Field"},{"venue_id":"407","name":"Woodlands Secondary School Field"},{"venue_id":"561","name":"Woodlands Secondary School Hall"},{"venue_id":"312","name":"Woodlands Sports Hall"},{"venue_id":"802","name":"Woodlands Sports Hall Meeting Room"},{"venue_id":"569","name":"Xing Hua Primary School"},{"venue_id":"951","name":"Xingnan Primary School Hall"},{"venue_id":"926","name":"Xishan Primary School Hall"},{"venue_id":"800","name":"Yio Chu Kang Conference Room"},{"venue_id":"946","name":"Yio Chu Kang Primary School Hall"},{"venue_id":"412","name":"Yio Chu Kang Secondary School Field"},{"venue_id":"450","name":"Yio Chu Kang Secondary School Hall"},{"venue_id":"314","name":"Yio Chu Kang Sports Hall"},{"venue_id":"281","name":"Yio Chu Kang Squash Centre"},{"venue_id":"283","name":"Yio Chu Kang Tennis Centre"},{"venue_id":"868","name":"Yishun Primary School Hall"},{"venue_id":"434","name":"Yishun Secondary School Hall"},{"venue_id":"316","name":"Yishun Sports Hall"},{"venue_id":"801","name":"Yishun Sports Hall - Meeting Room"},{"venue_id":"344","name":"Yishun Town Secondary School Hall"},{"venue_id":"922","name":"Yuan Ching Secondary School Field"},{"venue_id":"456","name":"Yuan Ching Secondary School Hall"},{"venue_id":"335","name":"Yusof Ishak Secondary School Field"},{"venue_id":"345","name":"Yusof Ishak Secondary School Hall"},{"venue_id":"435","name":"Yuying Secondary School Hall"},{"venue_id":"855","name":"Zhangde Primary School Hall"},{"venue_id":"448","name":"Zhonghua Primary School Hall"}]


def get_data_from_page(venue_id):
    import time, datetime
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(days=7)
    wanted_time = int(time.mktime(time.strftime("%Y-%m-%d", end_time)))
    paras = {
        'time_from': wanted_time,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'Host': 'members.myactivesg.com',
        'Referer': 'https://members.myactivesg.com/facilities/result?activity_filter=18&venue_filter=&date_filter=Wed%2C+5+Dec+2018&search=Search',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }

    url = 'https://members.myactivesg.com/facilities//view/activity/18/venue/{}?time_from={}'.format(venue_id, wanted_time)
    try:
        response = requests.get(url, params=paras, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None


# def parse_data(html):
    # pattern = re.compile('<a style=.*? target="_blank">(.*?)</a>.*?'
    #     '<td class="gsmc"><a href="(.*?)" target="_blank">(.*?)</a>.*?'
    #     '<td class="zwyx">(.*?)</td>', re.S)
    # pattern = 'PHPJS.venue_list'
    # items = re.findall(pattern, html)
    # print(items)
    # for item in items:
    #     job_name = item[0]
    #     job_name = job_name.replace('<b>', '')
    #     job_name = job_name.replace('</b>', '')
    #     yield {
    #         'job': job_name,
    #         'website': item[1],
    #         'company': item[2],
    #         'salary': item[3]
    #     }


# def write_csv_headers(filename, headers):
#     with open(filename, 'w') as f:
#         f_csv = csv.DictWriter(f, headers)
#         f_csv.writeheader()
def find_venue_list(html):
    soup = BeautifulSoup(html)
    venue_list = soup.find_all('PHPJS.venue_list')


def write_csv(filename, headers, rows):
    with open(filename, 'w') as f:
        # f_csv = csv.DictWriter(f, headers)
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def main(activity_code, venue, date):
    filename = 'badminton_court' + '_' + '.csv'
    headers = ['venue', 'date', 'time_slot', ]
    # write_csv_headers(filename, headers)
    '''
    get the data and save them to csv file
    '''
    jobs = []
    html = get_data_from_page(activity_code, venue, date)
    items = parse_data(html)
    for item in items:
        jobs.append(item)

    write_csv_rows(filename, headers, jobs)




if __name__ == '__main__':
    main('18', '', 'Sat%2C+24+Nov+2018')