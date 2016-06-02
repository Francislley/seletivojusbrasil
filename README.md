# processo_seletivo_jus_brasil
Trabalho desenvolvido como parte do processo seletivo da Jus Brasil
Consiste numa API que indexa e busca itens pré-cadastrados
Para criá-la, foi utilizado o Flask e o ElasticSearch
Para executá-la, deve-se:

Executar o ElasticSearch (pelo terminal):
$ ./engine/elasticsearch-2.3.3/bin/elasticsearch

Iniciar a API (abra outro terminal):
$ ./app.py
(pode ser necessário executar, antes: $ chmode a+x app.py)

Executar a API (abra um terceiro terminal)

Ela responde aos comandos POST e GET.
para POST (cadastro de documentos), o padrão é:
$ curl -H "Content-Type: application/json" -X POST -d '{"title": "Some title", "type": "TOPIC"}' http://localhost:5000/entities/
onde "Some Title" e "TOPIC" são qualque string que desejar

Para GET, o padrão é:
curl -XGET http://my-search-engine/entities/?q=som
onde "som" é um texto pertencente aos valores cadastrados em POST
