import requests
import json
import re
import tqdm


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "text/plain;charset=UTF-8",
    "origin": "https://v.qq.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://v.qq.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}
cookies = {
    "qq_domain_video_guid_verify": "698faf2eeb5f2b5a",
    "_qimei_uuid42": "1941b0e2313100af5e6ab6a49de97d2d8c78807e92",
    "vversion_name": "8.2.95",
    "video_omgid": "698faf2eeb5f2b5a",
    "pgv_pvid": "6016141815",
    "_qimei_fingerprint": "7da690b9075f5f3379579dc4c137428a",
    "_qimei_q36": "",
    "_qimei_h38": "aea30e555e6ab6a49de97d2d02000008b1941b",
    "o_minduid": "mS91bpCxKeblCJTHoUpcG2ovzjm9dnNR",
    "appuser": "E46565C0992C5FE4",
    "pgv_info": "ssid=s3174984890",
    "LZCturn": "306",
    "LPSJturn": "446",
    "LBSturn": "561",
    "LVINturn": "517",
    "LPHLSturn": "426",
    "LDERturn": "186",
    "LPPBturn": "453",
    "LZTturn": "65",
    "Lturn": "847",
    "LKBturn": "909",
    "LPVLturn": "193"
}
url = "https://vd6.l.qq.com/proxyhttp"
data = {
    "buid": "vinfoad",
    "vinfoparam": "charge=0&otype=ojson&defnpayver=3&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200m49hfid%2Fu4101r9hb9p.html&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200m49hfid%2Fu4101r9hb9p.html&sphttps=1&encryptVer=9.2&cKey=YXnpicVbwRa1EM1Orq2-LnCjnpb8Ocr0cPTRySfwzEul_f4uOWcvUGJNR8Gt67M9PBEK3hYG1moKCp7VHCeQghpmp7rG5tiHjLv_PnnatnPaZfOXktuBpd_Ilbpi-4KcjV30-IIK4INvFjOj-NmZhE-NjjawCzIdF66cdsFdzz5jk70UOmynTHDptaxqIemxrSlkg-M_BbDaBoWksGXkUJYnQqXKgvocvCDoQBra3Bby3kOuy43cijXGk2y1yg6T05LGGOeJuNIFi3m5pvAjoPAdvjeBPEfwmNLx9gg9S9d4Iprj18f4srmonrvmrcFLf9172-Nn84r3Le-qhtp4vqgEhJf4crMKM6WgP_EWl56z9lwdKyYQnLktXEYygRMgDrBidbEZKbFuyIJ04o47wa7kPYOcvcq-5VXKhYQhg4UO3pjLZlLFg-Hy4nz9tvgWJLTt9iauTd5VHF1l-njSiE0ZoqGCTidUsxFPB9A4WshjadiTBAQEBA2mI-M&clip=4&guid=698faf2eeb5f2b5a&flowid=fddb29f6a8739771726e7032748fc975&platform=10201&sdtfrom=v1010&appVer=1.42.3&unid=&auth_from=&auth_ext=&vid=u4101r9hb9p&defn=hd&fhdswitch=0&dtype=3&spsrt=2&tm=1745742370&lang_code=0&logintoken=&qimei=&spvvpay=1&spadseg=3&spav1=15&hevclv=28&spsfrhdr=0&spvideo=0&spm3u8tag=67&spmasterm3u8=3&track=undefined&atime=292&spcaptiontrack=1&drm=32",
    "sspAdParam": "{\"ad_scene\":1,\"pre_ad_params\":{\"ad_scene\":1,\"user_type\":0,\"video\":{\"base\":{\"vid\":\"u4101r9hb9p\",\"cid\":\"mzc00200m49hfid\"},\"is_live\":false,\"type_id\":2,\"referer\":\"\",\"url\":\"https://v.qq.com/x/cover/mzc00200m49hfid/u4101r9hb9p.html?j_vid=l30878tf337&j_cut_vid=q41017uax3d&j_is_win_vid=1\",\"flow_id\":\"fddb29f6a8739771726e7032748fc975\",\"refresh_id\":\"a8c370e1021261eaf2f81385e0cb2672_1745735722\",\"fmt\":\"hd\"},\"platform\":{\"guid\":\"698faf2eeb5f2b5a\",\"channel_id\":0,\"site\":\"web\",\"platform\":\"in\",\"from\":0,\"device\":\"pc\",\"play_platform\":10201,\"pv_tag\":\"www_google_com|顶部导航区:客户端\",\"support_click_scan_integration\":true},\"player\":{\"version\":\"1.41.1\",\"plugin\":\"4.1.31\",\"switch\":1,\"play_type\":\"0\"},\"token\":{\"type\":0,\"vuid\":0,\"vuser_session\":\"\",\"app_id\":\"\",\"open_id\":\"\",\"access_token\":\"\"},\"req_extra_info\":{\"now_timestamp_s\":1745742370,\"ad_frequency_control_time_list\":{},\"ad_request_id\":\"bcac7729-29e4-428c-84c6-3861649f9429\",\"exp_ids\":[\"100000\",\"11892118\"],\"video_played_time_ms\":0,\"playback_novelty_contexts\":[]},\"extra_info\":{}}}",
    "adparam": "adType=preAd&vid=u4101r9hb9p&sspKey=fowu"
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
json_data = response.json()

vinfo = json_data['vinfo']

info_json = json.loads(vinfo)


m3u8_url = info_json['vl']['vi'][0]['ul']['ui'][-1]['url']

m3u8 = requests.get(url=m3u8_url, headers=headers).text


ts_list = re.findall(',\n(.*?)\n#', m3u8)
ts_name = '/'.join(m3u8_url.split('/')[:-1]) + '/'
ts_time = int(re.findall('end=(.*?)&brs=', ts_list[-1])[0][0:4]) / 60

# for循环遍历
print(f'开始下载视频, 当前视频时长为{ts_time}')
for ts in tqdm.tqdm(ts_list):
    # 拼接完整的ts视频链接地址
    ts_url = ts_name + ts
    # 获取视频片段内容
    ts_content = requests.get(url=ts_url, headers=headers).content
    with open('MP4/111.mp4', mode='ab') as f:  # 这个地方的111.mp4 写的文件名（提前新建一个MP4文件）
        f.write(ts_content)


print(response.text)
print(response)