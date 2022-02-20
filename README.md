# わたしのくちぐせカウンター
テキストまたは音声ファイルからくちぐせをカウントするStreamlit製のウェブアプリです。

アプリページは[こちら](https://share.streamlit.io/sashimimochi/my-kuchiguse-cnt/main/app.py)

## Development
環境構築はDockerから作ることができます。

### Build
```bash
docker-compose build
```

### Start
```bash
docker-compose up -d
docker-compose exec kuchiguse streamlit run app.py
```

起動出来たら適当なブラウザで http://localhost:8501 にアクセスすればローカルで立ち上げたアプリにアクセスできます。
