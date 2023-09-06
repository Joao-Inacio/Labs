# Documentação MongoDB Básica

## 1. Inserção de Documentos

**Inserir um único documento:**

```javascript
db('dbmidias').collection('posts').insertOne({
    nome: "José", 
    postagem: "Bons Produtos!", 
    data: "31-06-2019"
});
```

**Inserir vários documentos:**

```javascript
db('dbmidias').collection('posts').insertMany([
    {nome : "Antonio", postagem: "Minha bike quebrou", data: "26-05-2019"},
    {nome: "Maria Silva", postagem: "Encontrei tudo que procurava", data: "14-06-2019"},
    // ... (outros documentos)
]);
```

## 2. Consulta de Documentos

**Buscar todos os documentos em uma coleção:**

```javascript
db('dbmidias').collection('posts').find().toArray();
```

**Buscar um único documento:**

```javascript
db('dbmidias').collection('posts').findOne();
```

**Buscar com filtros e apresentar de forma "bonita":**

```javascript
db('dbmidias').collection('posts').find({nome: "José"}).pretty();
```

## 3. Atualização de Documentos

**Atualizar um documento:**

```javascript
db('dbmidias').collection('posts').updateOne(
    {nome: "José"},
    {$set: {idade: 29}}
);
```

**Atualizar múltiplos documentos:**

```javascript
db('dbmidias').collection('posts').updateMany(
    {nome: "José"},
    {$set: {idade: 28}}
);
```

## 4. Exclusão de Documentos

**Excluir um documento:**

```javascript
db('dbmidias').collection('posts').deleteOne({nome: "José"});
```

**Excluir múltiplos documentos:**

```javascript
db('dbmidias').collection('posts').deleteMany({nome: "José"});
```

## 5. Exclusão de Coleções e Bancos de Dados

**Excluir uma coleção:**

```javascript
db('dbmidias').collection('posts').drop();
```

**Excluir um banco de dados:**

```javascript
db('dbmidias').dropDatabase();
```

## 6. Importação de Documentos

**Para importar documentos de um arquivo JSON para uma coleção:**

```sh
mongoimport --db escola --collection estudante --file estudantes.json --jsonArray
```

**Para importar documentos usando código:**

```javascript
db('escola').collection('estudantes').insertMany([
    {"_id":0,"name":"aimee Zank","scores":[...]},
    // ... (outros documentos)
]);
```

Essa é uma visão geral dos comandos básicos do MongoDB que discutimos. Lembre-se sempre de consultar a documentação oficial do MongoDB para obter informações detalhadas e atualizadas sobre cada comando e método.
