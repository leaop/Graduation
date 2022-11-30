library(dplyr)
library(dslabs)
library(readr)
library(data.table)
#dados originais (direto do python)
View(Dados_R)
str(Dados_R)
#pegar os 10 primeiros em ordem
Dados_R %>% top_n(10, EXACT_MASS)
Dados_R %>% top_n(10, NumHAcceptors)
Dados_R %>% top_n(10, NumHDonors)
Dados_R %>% top_n(10, RingCount)
Dados_R %>% top_n(10, TPSA)
Dados_R %>% top_n(10, RotatableBond)
#sumário dos dados
summary(Dados_R)
#criacao de um indice logico dentro de coluna sem desenho
ind <- is.na(Dados_R$ROMol)
#determinar a media de valores da massa
mean(Dados_R$EXACT_MASS)
#qual formula possui maior massa
dados$FORMULA[which.max(dados$EXACT_MASS)]
#as formulas até agora estão dando errado pois possuem colunas ainda com NA, é preciso filtrar



#limpando os dados
dadosS <- Dados_R %>% filter(SMILES != "NA" )
dadosF <- dadosS %>% filter(FORMULA != "NA" )
dadosEM <- dadosF %>% filter(EXACT_MASS != "NA") 
dadosA <- dadosEM %>% filter(NumHAcceptors != "NA")
#somente nesse ponto foram tirados todos os NA, mas a verificação de limpeza continuou
dadosD <- dadosA %>% filter(NumHDonors != "NA")
dadosC <- dadosD %>% filter(RingCount != "NA")
dadosT <- dadosC %>% filter(TPSA != "NA")
dados <- dadosT %>% filter(RotatableBond != "NA")

#sumarizando
summary(dados)
#quantos dados tem em cada quartil
quantile(dados$EXACT_MASS, probs = seq(.1,1, by = .05))
quantile(dados$NumHAcceptors, probs = seq(.25,1, by = .05))
quantile(dados$NumHDonors, probs = seq(.5,1, by = .05))
quantile(dados$RingCount, probs = seq(.75,1, by = .05))
quantile(dados$TPSA, probs = seq(.25,1, by = .05))
quantile(dados$RotatableBond, probs = seq(.25,1, by = .05))

#pegar os 10 primeiros em ordem depois do tratamento
dados %>% top_n(10, EXACT_MASS)
dados %>% top_n(10, NumHAcceptors)
dados %>% top_n(10, NumHDonors)
dados %>% top_n(10, RingCount)
dados %>% top_n(10, TPSA)
dados %>% top_n(10, RotatableBond)

#trabalhando com dataset
dadosT <- setDT(dadosT)
#selecionar colunas especificas
dadosT[, c("GenericName", "SMILES")] |> head()
dadosT[, c("GenericName", "RingCount")] |> head()
dadosT[, c("GenericName", "TPSA")] |> head()
dadosT[, c("GenericName", "NumHDonors")] |> head()
dadosT[, c("GenericName", "NumHAcceptors")] |> head()
dadosT[, c("GenericName", "EXACT_MASS")] |> head()

#maiores dados em geral
max(dados$EXACT_MASS)
max(dados$NumHAcceptors)
max(dados$NumHDonors)
max(dados$RingCount)
max(dados$TPSA)
max(dados$RotatableBond)
max(dados$LogP)

#determinar a media de valores em geral
mean(dados$EXACT_MASS)
mean(dados$NumHAcceptors)
mean(dados$NumHDonors)
mean(dados$RingCount)
mean(dados$TPSA)
mean(dados$RotatableBond)
mean(dados$LogP)

#tabela com os valores acima
MM <- data.frame(ID = c("Exact mass", "Num Acceptors", "Num Donors", "Ring Count", "TPSA", "Rotatable Bond", "LogP"),
                 Max = c(max(dados$EXACT_MASS),
                         max(dados$NumHAcceptors),
                         max(dados$NumHDonors),
                         max(dados$RingCount),
                         max(dados$TPSA),
                         max(dados$RotatableBond),
                         max(dados$LogP)),
                 Mean = c(mean(dados$EXACT_MASS),
                          mean(dados$NumHAcceptors),
                          mean(dados$NumHDonors),
                          mean(dados$RingCount),
                          mean(dados$TPSA),
                          mean(dados$RotatableBond),
                          mean(dados$LogP)),
                 stringsAsFactors = FALSE)

#comparacao entre vetores
index <- match(dados$GenericName, dados$RotatableBond)
dados$RotatableBond[index]

#agrupando e sumarizando
dados %>% group_by(TPSA) %>% summarise(median = median(RotatableBond))

#mostrar os menores em RingCount
dados %>% arrange(RingCount) %>% head()

#os menores agrupados por outro item
dados %>% arrange(TPSA, EXACT_MASS) %>% head()



#qual formula possui maiores valores
dados$FORMULA[which.max(dados$EXACT_MASS)]
dados$FORMULA[which.max(dados$NumHAcceptors)]
dados$FORMULA[which.max(dados$NumHDonors)]
dados$FORMULA[which.max(dados$RingCount)]
dados$FORMULA[which.max(dados$TPSA)]
dados$FORMULA[which.max(dados$RotatableBond)]
dados$FORMULA[which.max(dados$LogP)]
FOR <- dados %>% select(FORMULA, GenericName) %>% filter( FORMULA== "C128H212N2O27P2" | FORMULA== "C62H121NO26P2" | FORMULA==  "C56H42O12" | FORMULA== "C6H20O30P8" | FORMULA== "C81H152O17P2" | FORMULA== "C110H180O7P2")

#juntando com o dataframe anterior
#opcoes de usar o rbind: iria combinar o FOR com o MM, contanto que adicionasse uma linha a mais no FOR
#posso criar nova lista e adicionar ao MM
c1 <- c(dados$FORMULA[which.max(dados$EXACT_MASS)],
        dados$FORMULA[which.max(dados$NumHAcceptors)],
        dados$FORMULA[which.max(dados$NumHDonors)],
        dados$FORMULA[which.max(dados$RingCount)],
        dados$FORMULA[which.max(dados$TPSA)],
        dados$FORMULA[which.max(dados$RotatableBond)],
        dados$FORMULA[which.max(dados$LogP)])
MM <- mutate(MM, Formula=c1)
#agora vou adicionar a outra com os nomes genéricos, com o FOR tenho a lista de nomes
dados %>% select(FORMULA, GenericName) %>% filter( FORMULA== "C128H212N2O27P2"| FORMULA== "C62H121NO26P2" | FORMULA==  "C56H42O12" | FORMULA== "C6H20O30P8" | FORMULA== "C81H152O17P2" | FORMULA== "C110H180O7P2")
c2 <- c("alpha-D-mannosyl-beta-D-mannosyldiacetylchitobiosyldiphosphodolichol", "alpha-D-mannosyl-beta-D-mannosyldiacetylchitobiosyldiphosphodolichol", "inositol phosphomannosylinositol phosphoceramide", "Hopeaphenol", "5,6-Bis(diphospho)-1D-myo-inositol tetrakisphosphate", "CL(1'-[18:0/18:1(9Z)],3'-[18:1(9Z)/18:1(9Z)])", "docosaprenyl diphosphate")
MM <- mutate(MM, Generic_name=c2)


#qual a formula que possui maior massa por ligações
massR <- dados$EXACT_MASS/dados$RingCount
order <- dados$FORMULA[order(massR, decreasing = TRUE)]
ord <- data.frame(order)

#plot entre dados
plot(dados$EXACT_MASS,dados$RingCount)
plot(dados$EXACT_MASS,dados$NumHAcceptors)
plot(dados$EXACT_MASS,dados$NumHDonors)
plot(dados$EXACT_MASS,dados$TPSA)

#plot por dist. normal
var(dados$EXACT_MASS)
sd(dados$EXACT_MASS)
mean(dados$EXACT_MASS)
m <- dnorm(dados$EXACT_MASS, mean = 478.3007, sd = 327.7294)
plot (dados$EXACT_MASS,m,type = "l",lwd=4,col="darkred")

var(dados$NumHAcceptors)
sd(dados$NumHAcceptors)
mean(dados$NumHAcceptors)
a <- dnorm(dados$NumHAcceptors, mean = 5.095789, sd = 4.071929)
plot (dados$NumHAcceptors,a)

var(dados$NumHDonors)
sd(dados$NumHDonors)
mean(dados$NumHDonors)
d <- dnorm(dados$NumHDonors, mean = 2.413158, sd = 3.01468)
plot (dados$NumHDonors,d)

var(dados$RingCount)
sd(dados$RingCount)
mean(dados$RingCount)
r <- dnorm(dados$RingCount, mean = 0.7863158, sd = 1.300392)
plot (dados$RingCount,r)

var(dados$TPSA)
sd(dados$TPSA)
mean(dados$TPSA)
t <- dnorm(dados$TPSA, mean = 111.7867, sd = 82.96118)
plot (dados$TPSA,t)

var(dados$RotatableBond)
sd(dados$RotatableBond)
mean(dados$RotatableBond)
b <- dnorm(dados$RotatableBond, mean = 19.67579, sd = 19.03001)
plot (dados$RotatableBond,b)


#Boxplot das maiores massas/ligações
boxplot(dados$EXACT_MASS, ylab="Mass")
boxplot(EXACT_MASS ~ RingCount, data = dados, xlab = "RCount",
        ylab = "Mass", main = "Test2")

#histograma
date <- mutate(dados, rate = massR)
hist(date$rate)
hist(dados$EXACT_MASS)
hist(dados$NumHAcceptors)
hist(dados$NumHDonors)
hist(dados$RingCount)
hist(dados$TPSA)

#extração de planilhas para fora do R Studio
write.csv(MM, file='MM.csv')#atribuição do nome do arquivo

#plot com cor
install.packages("tidyverse")
library(tidyverse)
ggplot(data=dados)+ geom_point(mapping= aes(x=EXACT_MASS, y=RingCount)) + facet_wrap(~ HumHAcceptors, nrow=2)


ggplot(data=dados) +
  geom_point(mapping= aes(x=EXACT_MASS, y=NumHDonors)) +
  geom_smooth(mapping= aes(x=EXACT_MASS, y=NumHDonors))

ggplot(data = dados, mapping = aes(x=EXACT_MASS, y=NumHAcceptors)) + geom_point() + geom_smooth()

ggplot(data = dados, mapping = aes(x = EXACT_MASS, y=TPSA)) + geom_point(mapping = aes(color = RingCount)) + geom_smooth()

ggplot(data = dados, mapping = aes(x = EXACT_MASS, y=RingCount)) + geom_point() + geom_smooth(se=FALSE)

ggplot(data = dados, mapping = aes(x = NumHDonors, y=RingCount, color=TPSA)) + 
  geom_point() +
  geom_smooth(se = FALSE)

ggplot(data = dados, mapping = aes(x =EXACT_MASS, y=RingCount)) + 
  geom_point(mapping = aes(color=TPSA)) +
  geom_smooth(se = FALSE)

ggplot(data = dados, mapping = aes(x =EXACT_MASS, y=RingCount)) +
  geom_point(size=4, color="white") +
  geom_point(aes(color=NumHDonors))




