# Comandos

### 1. Alterar separador para vírgula e imprimir ID do Sensor e Local
```
awk -F',' 'BEGIN{OFS=","} {print $3,$4}' sensores.log
```

### 2. Excluir a primeira linha (cabeçalho) antes de exibir
```
sed '1d' sensores.log
```

### 3. Ignorar o cabeçalho e imprimir linhas com Temperatura maior que 25.0
```
awk -F',' 'NR > 1 && $5 > 25.0 {print}' sensores.log
```

### 4. Substituir todas as ocorrências de DataCenter por Servidores
```
sed 's/DataCenter/Servidores/g' sensores.log
```

### 5. Filtrar status OK e contar o total de leituras normais
```
awk -F',' '$7 == "OK" {count++} END {print count}' sensores.log
```

### 6. Remover todas as linhas que contenham a palavra ERRO
```
sed '/ERRO/d' sensores.log
```

### 7. Calcular a média das temperaturas desconsiderando o cabeçalho
```
LANG=C awk -F',' 'NR > 1 {soma += $5; count++} END {print soma / count}' sensores.log
```

### 8. Substituir os hifens das datas (coluna 1) por barras
```
sed 's/^\([0-9]\{4\}\)-\([0-9]\{2\}\)-\([0-9]\{2\}\)/\1\/\2\/\3/' sensores.log
```

### 9. Contar quantas vezes cada sensor enviou dados
```
awk -F',' 'NR > 1 {sensores[$3]++} END {for (s in sensores) print s, sensores[s]}' sensores.log
```

### 10. Substituir CRITICO_TEMP por EMERGENCIA e imprimir apenas as linhas alteradas
```
sed -n 's/CRITICO_TEMP/EMERGENCIA/p' sensores.log
```

### 11. Substituir vírgulas por espaços e imprimir a 2ª e a 5ª colunas
```
sed 's/,/ /g' sensores.log | awk '{print $2, $5}'
```

### 12. Encontrar a temperatura mais alta registrada
```
awk -F',' 'NR > 1 {if ($5 > max) max = $5} END {print max}' sensores.log
```

### 13. Adicionar [INSPECIONADO] no final das linhas com o sensor SNSR-01
```
sed '/SNSR-01/s/$/ [INSPECIONADO]/' sensores.log
```

### 14. Exibir o Local alinhado à esquerda com 15 caracteres e a Umidade
```
awk -F',' 'NR > 1 {printf "%-15s %s\n", $4, $6}' sensores.log
```

### 15. Filtrar leituras do Armazém e somar o total de umidades
```
grep ",Armazem," sensores.log | LANG=C awk -F',' '{soma += $6} END {print soma}'
```
