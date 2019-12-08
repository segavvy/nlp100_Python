# nlp100_Python
[言語処理100本ノック 2015](http://www.cl.ecei.tohoku.ac.jp/nlp100/)の挑戦記録のまとめです。解説は以下のQiitaへのリンクを参照してください。

#挑戦した環境
Ubuntu 16.04 LTS ＋ Python 3.5.2 \:\: Anaconda 4.1.1 (64-bit)です。
（[問題00](http://qiita.com/segavvy/items/709c6e2d156b7837b3a8)と[問題01](http://qiita.com/segavvy/items/966c7b658ca740f6164b)だけはPython 2.7です。）

#第1章: 準備運動
>テキストや文字列を扱う題材に取り組みながら，プログラミング言語のやや高度なトピックを復習します．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題00](http://qiita.com/segavvy/items/709c6e2d156b7837b3a8)|スライス、`print()`|
|[問題01](http://qiita.com/segavvy/items/966c7b658ca740f6164b)|スライス|
|[問題02](http://qiita.com/segavvy/items/725b20f21951975a06fd)|Anaconda、`zip()`、`itertools.zip_longest()`、イテラブルの前に`*`をつけると引数にバラしてくれる、`str.join()`、`functools.reduce()`|
|[問題03](http://qiita.com/segavvy/items/a0ddefb64cc878b9639b)|`len()`、`list.append()`、`str.split()`、`list.count()`|
|[問題04](http://qiita.com/segavvy/items/4e592dea2f828e5385ff)|`enumerate()`、Python3.3以降ではデフォルトでハッシュがランダム化される|
|[問題05](http://qiita.com/segavvy/items/6f9f028914176c069c41)|n-gram、`range()`|
|[問題06](http://qiita.com/segavvy/items/209bf27d4cee51f60f99)|`set()`、`set.union()`、 `set.intersection()`、 `set.difference()`|
|[問題07](http://qiita.com/segavvy/items/6967ab5e8d41c7a879db)|`str.format()`、`string.Template`、`string.Template.substitute()`|
|[問題08](http://qiita.com/segavvy/items/5552623de614ca3344df)|`chr()`、`str.islower()`、`input()`、3項演算子|
|[問題09](http://qiita.com/segavvy/items/be0f59af4b410069516d)|Typoglycemia、`random.shuffle()`|

#第2章: UNIXコマンドの基礎
>研究やデータ分析において便利なUNIXツールを体験します．これらの再実装を通じて，プログラミング能力を高めつつ，既存のツールのエコシステムを体感します．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題10](http://qiita.com/segavvy/items/9b14293e50dec0c4b242)|[UNIXコマンド]`man`の日本語化、`open()`、シェルスクリプト、[UNIXコマンド]`wc`,`chmod`、ファイルの実行権限|
|[問題11](http://qiita.com/segavvy/items/85e78ce405daf10d0ed6)|`str.replace()`、[UNIXコマンド]`sed`、`tr`、`expand`|
|[問題12](http://qiita.com/segavvy/items/51a515c19bcd29b13b7f)|`io.TextIOBase.write()`、[UNIXコマンド]`cut`,`diff`、UNIXコマンドの短いオプションと長いオプション|
|[問題13](http://qiita.com/segavvy/items/ec9a3846f779c81e3d10)|[UNIXコマンド]`paste`、`str.rstrip()`、Pythonの「空白文字」の定義|
|[問題14](http://qiita.com/segavvy/items/53271a1327bb3c8c5457)|[UNIXコマンド]`echo`,`read`,`head`|
|[問題15](http://qiita.com/segavvy/items/c2675e44ea05c56995e3)|`io.IOBase.readlines()`、[UNIXコマンド]`tail`|
|[問題16](http://qiita.com/segavvy/items/993ea169a1111c6f6f69)|[UNIXコマンド]`split`、`math.ceil()`、`str.format()`、`//`で切り捨ての除算ができる|
|[問題17](http://qiita.com/segavvy/items/202e61ce4e4cccc29d06)|`set.add()`、[UNIXコマンド]`cut`,`sort`,`uniq`|
|[問題18](http://qiita.com/segavvy/items/adee520db1a257e347d5)|ラムダ式|
|[問題19](http://qiita.com/segavvy/items/58f11bce5f786e590d98)|リストの内包表記、`itertools.groupby()`、`list.sort()`|

#第3章: 正規表現
>Wikipediaのページのマークアップ記述に正規表現を適用することで，様々な情報・知識を取り出します．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題20](http://qiita.com/segavvy/items/dc1e63fd8f7bd5d99eea)|JSONの操作、`gzip.open()`、`json.loads()`|
|[問題21](http://qiita.com/segavvy/items/73f1b91ff75529ae3b8d)|正規表現、raw string記法、`raise`、`re.compile()`、`re.regex.findall()`|
|[問題22](http://qiita.com/segavvy/items/3e7de80f88c2c1096bef)|[正規表現]貪欲マッチ,非貪欲マッチ|
|[問題23](http://qiita.com/segavvy/items/691ac169dd5b36e6a187)|[正規表現]後方参照|
|[問題24](http://qiita.com/segavvy/items/03b97eb6a39f5ae6aa34)||
|[問題25](http://qiita.com/segavvy/items/e402ad0a5b0f52453d7f)|[正規表現]肯定の先読み、`sorted()`|
|[問題26](http://qiita.com/segavvy/items/f6d0f3d6eee5acc33c58)|`re.regex.sub()`|
|[問題27](http://qiita.com/segavvy/items/9a8137f045852bc299d6)||
|[問題28](http://qiita.com/segavvy/items/8c4567ec1124320d3354)||
|[問題29](http://qiita.com/segavvy/items/fc7257012d8a590185e5)|Webサービスの利用、`urllib.request.Request()`、`urllib.request.urlopen()`、`bytes.decode()`|

#第4章: 形態素解析
>夏目漱石の小説『吾輩は猫である』に形態素解析器MeCabを適用し，小説中の単語の統計を求めます．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題30](http://qiita.com/segavvy/items/1f517e06aa3bc5fc2316)|conda、pip、apt、[MeCab]インストール,使い方、形態素解析、ジェネレータ、`yield`|
|[問題31](http://qiita.com/segavvy/items/e63d90c675dad7d8bb42)|[形態素解析]表層形|
|[問題32](http://qiita.com/segavvy/items/64920712cc4b12e8ce51)|[形態素解析]原形・基本形、リストの内包表記|
|[問題33](http://qiita.com/segavvy/items/229d0a672a866b3e09a1)|[形態素解析]サ変接続の名詞、2重ループのリストの内包表記|
|[問題34](http://qiita.com/segavvy/items/92f1177b6f095eb686a8)||
|[問題35](http://qiita.com/segavvy/items/bda3a16d8bb54bd01f73)|[形態素解析]名詞の連接|
|[問題36](http://qiita.com/segavvy/items/932c1413e2552f208dfc)|`collections.Counter`、`collections.Counter.update()`|
|[問題37](http://qiita.com/segavvy/items/72863888e51fabd79295)|[matplotlib]インストール,棒グラフ,日本語表示,軸の範囲,グリッド表示|
|[問題38](http://qiita.com/segavvy/items/c53c35827524f875ba2d)|[matplotlib]ヒストグラム|
|[問題39](http://qiita.com/segavvy/items/e0a7994cc63c8be7380b)|[matplotlib]散布図、Zipfの法則|


#第5章: 係り受け解析
>『吾輩は猫である』に係り受け解析器CaboChaを適用し，係り受け木の操作と統語的な分析を体験します．


| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題40](http://qiita.com/segavvy/items/2f686cfb0065c8cbe698)|[CaboCha]インストール,使い方、`__str__()`、`__repr__()`、`repr()`|
|[問題41](http://qiita.com/segavvy/items/003e8b7e0f132f4fde1b)|[係り受け解析]文節と係り受け|
|[問題42](http://qiita.com/segavvy/items/58894f76dba367b2925b)||
|[問題43](http://qiita.com/segavvy/items/30d14259aa350f88852f)||
|[問題44](http://qiita.com/segavvy/items/d1a9a8d87d8dc10a8f15)|[pydot-ng]インストール,有向グラフ、Pythonで作られているモジュールのソースの確認方法|
|[問題45](http://qiita.com/segavvy/items/2f8387a5973a9966a12d)|[係り受け解析]格、[UNIXコマンド]`grep`|
|[問題46](http://qiita.com/segavvy/items/25511a18ad7928e3982f)|[係り受け解析]格フレーム・格文法|
|[問題47](http://qiita.com/segavvy/items/c40bbafef33c65f6c6ad)|[係り受け解析]機能動詞|
|[問題48](http://qiita.com/segavvy/items/ed5cc48dc02afd8855a1)|[係り受け解析]名詞から根へのパス|
|[問題49](http://qiita.com/segavvy/items/dfbf9d5dd5885e807d49)|[係り受け解析]名詞間の係り受けパス|

#第6章: 英語テキストの処理
>Stanford Core NLPを用いた英語のテキスト処理を通じて，自然言語処理の様々な基盤技術を概観します．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題50](http://qiita.com/segavvy/items/05d5846bb77c6829f76f)|ジェネレータ|
|[問題51](http://qiita.com/segavvy/items/f25fd2ff572cc8ec0534)||
|[問題52](http://qiita.com/segavvy/items/d47fa799883ed16eddc2)|語幹、ステミング、snowballstemmer：使い方|
|[問題53](http://qiita.com/segavvy/items/ab6bb2b994aac061f51f)|[Stanford Core NLP]インストール,使い方、`subprocess.run()`、XMLの解析、`xml.etree.ElementTree.ElementTree.parse()`、`xml.etree.ElementTree.ElementTree.iter()`|
|[問題54](http://qiita.com/segavvy/items/4d55805352089332828e)|[Stanford Core NLP]品詞,レンマ、XMLの解析、`xml.etree.ElementTree.Element.findtext()`|
|[問題55](http://qiita.com/segavvy/items/32b3a35825ec32586f33)|[Stanford Core NLP]固有表現、XPath、`xml.etree.ElementTree.Element.iterfind()`|
|[問題56](http://qiita.com/segavvy/items/0340d3d71c9151265bcb)|[Stanford Core NLP]共参照|
|[問題57](http://qiita.com/segavvy/items/d47b865c05be42b9d6d3)|[Stanford Core NLP]係り受け、[pydot-ng]有向グラフ|
|[問題58](http://qiita.com/segavvy/items/f100fc38e350ad14b679)|[Stanford Core NLP]主語,述語,目的語|
|[問題59](http://qiita.com/segavvy/items/0c14bcc7f6a983554637)|[Stanford Core NLP]句構造解析,S式、再帰呼び出し、`sys.setrecursionlimit()`、`threading.stack_size()`|

#第7章: データベース
>Key Value Store (KVS) やNoSQLによるデータベースの構築・検索を修得します．また，CGIを用いたデモ・システムを開発します．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題60](http://qiita.com/segavvy/items/14216054ef9becee7b3b)|[LevelDB]インストール,使い方、`str.encode()`、`bytes.decode()`|
|[問題61](http://qiita.com/segavvy/items/41b860ca0d0c7d8facc9)|[LevelDB]検索、Unicodeコードポイント、`ord()`|
|[問題62](http://qiita.com/segavvy/items/139a801550409d635803)|[LevelDB]列挙|
|[問題63](http://qiita.com/segavvy/items/507a82ecd75d0c6ea14f)|JSONの操作、`json.dumps()`|
|[問題64](http://qiita.com/segavvy/items/8f93187ec89f4831d863)|[MongoDB]インストール,使い方,インタラクティブシェル,バルクインサート,インデックス|
|[問題65](http://qiita.com/segavvy/items/d360c2568b49bd5c153a)|[MongoDB]検索,ObjectId、JSON形式の変換表にない型の扱い|
|[問題66](http://qiita.com/segavvy/items/8b4815ac4916fa6dd2e1)||
|[問題67](http://qiita.com/segavvy/items/efa40d47ab851c1aac52)||
|[問題68](http://qiita.com/segavvy/items/7da17f5ca81b28abe637)|[MongoDB]ソート|
|[問題69](http://qiita.com/segavvy/items/a8ed8a91ed2c6b834923)|Webサーバー、CGI、HTMLエスケープ、`html.escape()`、`html.unescape()`、[MongoDB]複数条件の検索|

#第8章: 機械学習
>評判分析器（ポジネガ分析器）を機械学習で構築します．さらに，手法の評価方法を学びます．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題70](http://qiita.com/segavvy/items/0e91fe02088b875a386a)|[機械学習]自動分類,ラベル,教師あり学習・教師なし学習|
|[問題71](http://qiita.com/segavvy/items/007ed0523bf4e79e12fb)|ストップワード、アサーション、`assert`|
|[問題72](http://qiita.com/segavvy/items/6695f94c28126607227b)|[機械学習]素性|
|[問題73](http://qiita.com/segavvy/items/5ad0d5742a674bdf56cc)|[NumPy]インストール,行列演算、[機械学習]ロジスティック回帰,ベクトル化,仮説関数,シグモイド関数,目的関数,最急降下法,学習率と繰り返し回数|
|[問題74](http://qiita.com/segavvy/items/8a46a74e7a88df89051d)|[機械学習]予測|
|[問題75](http://qiita.com/segavvy/items/5ded025346c9621aedb2)|[機械学習]素性の重み、[NumPy]ソートした結果のインデックス取得|
|[問題76](http://qiita.com/segavvy/items/e107f764534f01c5b105)||
|[問題77](http://qiita.com/segavvy/items/9444aecd0345a532fc9d)|正解率、適合率、再現率、F1スコア|
|[問題78](http://qiita.com/segavvy/items/50820438fd6d10ceba7d)|[機械学習]5分割交差検定|
|[問題79](http://qiita.com/segavvy/items/68e5661351da52f1d765)|[matplotlib]折れ線グラフ|

#第9章: ベクトル空間法 (I)
>大規模なコーパスから単語文脈共起行列を求め，単語の意味を表すベクトルを学習します．その単語ベクトルを用い，単語の類似度やアナロジーを求めます．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題80](http://qiita.com/segavvy/items/ea485e66dd96eee891da)|単語のベクトル化、`bz2.open()`|
|[問題81](http://qiita.com/segavvy/items/216888c3549cea3d8e81)|[単語ベクトル]複合語の対処|
|[問題82](http://qiita.com/segavvy/items/a8e269294f2c834cff08)||
|[問題83](http://qiita.com/segavvy/items/614689e7c4e2ba387929)|オブジェクトの直列化・シリアライズ、`pickle.dump()`、`pickle.load()`|
|[問題84](http://qiita.com/segavvy/items/21455b802e34a9e49f92)|[単語ベクトル]単語文脈行列,PPMI（正の相互情報量）、[SciPy]インストール,疎行列の扱い,直列化、`collections.OrderedDict`|
|[問題85](http://qiita.com/segavvy/items/f1a7f3200c3b771e8568)|主成分分析（PCA）、[scikit-learn]インストール,PCA|
|[問題86](http://qiita.com/segavvy/items/d0cfabf328fd6d67d003)||
|[問題87](http://qiita.com/segavvy/items/663454567a191cf1b968)|コサイン類似度|
|[問題88](http://qiita.com/segavvy/items/26ec387217b030a15c21)||
|[問題89](http://qiita.com/segavvy/items/2d21c9b5ab7e338dcf51)|加法構成性、アナロジー|

#第10章: ベクトル空間法 (II)
>word2vecを用いて単語の意味を表すベクトルを学習し，正解データを用いて評価します．さらに，クラスタリングやベクトルの可視化を体験します．

| Qiitaへのリンク | 主に学んだこと、コメントで教えていただいたことなど |
|:--:|--------|
|[問題90](http://qiita.com/segavvy/items/890d34a40991dd634cdf)|[word2vec]インストール,使い方|
|[問題91](http://qiita.com/segavvy/items/be511b97bf3be49974a3)||
|[問題92](http://qiita.com/segavvy/items/1d35a37c5d9faf9f636e)||
|[問題93](http://qiita.com/segavvy/items/f1939cabfc9f71e5aaa0)||
|[問題94](http://qiita.com/segavvy/items/4c3295bf2c0321bea5e2)||
|[問題95](http://qiita.com/segavvy/items/6181994f5667ee1fbebf)|スピアマンの順位相関係数、インスタンスへの動的メンバー追加、`**`でべき乗ができる|
|[問題96](http://qiita.com/segavvy/items/650c3e1254d8c5aef8e1)||
|[問題97](http://qiita.com/segavvy/items/e38710fed6c1cb8c5d2d)|クラシフィケーション、クラスタリング、K-Means、[scikit-learn]K-Means|
|[問題98](http://qiita.com/segavvy/items/5efe20750b643a2d49cb)|階層的クラスタリング、Ward法、デンドログラム、[SciPy]Ward法,デンドログラム|
|[問題99](http://qiita.com/segavvy/items/fe530927df30732e2a46)|t-SNE、[scikit-learn]t-SNE、[matplotlib]ラベル付き散布図|
