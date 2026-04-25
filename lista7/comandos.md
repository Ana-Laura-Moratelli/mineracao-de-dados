# Comandos

### 1. Imprimir IP e URL acessada
```
awk '{print $1, $7}' acessos.log
```

### 2. Excluir a primeira linha antes de exibir
```
sed '1d' acessos.log
```

### 3. Ignorar a primeira linha e imprimir acessos com status maior que 400
```
awk 'NR > 1 && $9 > 400 {print}' acessos.log
```

### 4. Substituir todas as ocorrências de catalogo.html por produtos.html
```
sed 's/catalogo.html/produtos.html/g' acessos.log
```

### 5. Contar quantas requisições tiveram status 200
```
awk '$9 == 200 {count++} END {print count}' acessos.log
```

### 6. Remover todas as linhas que contenham erro 404
```
sed '/404/d' acessos.log
```
