library(dslabs)

data(murders)
class(murders)
str(murders)
head(murders)
murders$population #accessor $
names(murders)

pop <- murders$population
length(pop)
class(pop)
class(murders$state)

z <- 3 == 2
class(z)

class(murders$region)
murders$region
length(murders$region)
levels(murders$region)
length(levels(murders$region))

murders$region == murders[["region"]]
murders[["region"]]
murders$region #O mais recomendado

class(murders[["region"]]) #factor
class(murders["region"])   #data.frame

x <- c("a","a","b","b","b","c")
class(x)
x
length(x)
levels(x)

table(x) #faz um quadro contando as repetições

a<-2
b<- -1
c<- -4

raiz1 <- (-b + sqrt(b^2-4*a*c))/(2*a)
raiz2 <- (-b - sqrt(b^2-4*a*c))/(2*a)

log(1024,4)

data(movielens)                         #carregar data frame
nrow(movielens)                         #numero de linhas
length(movielens)                       #numero de colunas
class(movielens$title)                  #tipo da variavel title
class(movielens$genres)                 #tipo da variavel genres
length(levels(movielens$genres))        #quantidade de generos


head(movielens)
str(movielens)



codes <- c(380,124,818)
country <- c("Italy", "Canada", "Egypt")
class(codes)
class(country)

names(codes) <- country    #atribui a codes os nomes de country
codes


codes <- c(italy=380,canada=124,egypt=818)
class(codes)
codes <- c("italy"=380,"canada"=124,"egypt"=818)
class(codes)

seq(1,10)
seq(10, 1, -0.1)  #sequencia de 1 a 10 andando 0.1 por vez
1:10

codes[2]            #segundo elemento
codes[c(1,3)]       #primeiro e terceiro elemento
codes[c(3,2,1)]
codes[c(seq(1,3,2))]
codes[1:2]
codes["Canada"]
codes[c("Egypt", "Italy")]

c(1,2,3,4) == c(seq(1,4))

x <- c(1,"Canada",3)
class(x)


x <- 1:5
y <- as.character(x)
y
y <- as.numeric(y)
y

temp <- c(50,75,90,100,150)

city <- c("Brasilia", "Paris", "Japonvar", "Itu", "Roma")

names(temp) <- city
temp

city <- c("Brasilia", "Paris", "Japonvar", "Itu")

names(temp) <- city
temp

temp[1:3]
temp[c("Paris", "Itu")]

x <- seq(13,71)
x
length(x)
sum(x[1:3])

sum(x[seq(1,71,2)])

x <- seq(13,71,2)
x
sum(x)


z <- seq(0,300, 7)  #Multiplos de 7 que são menores ou iguais a 300
z

impares <- seq(1,100,2)
impares

length(seq(6,55,4/7))

v <- seq(0,7, length.out = 5)
v

j <- seq(1,10, length.out = 100)
j


h<- vector("logical", length = 15)
h

class(3)
class(3L)

vetor <- c(1,3,5,"a")
class(vetor)                #COERSAO
class(vetor[1])

teste <- as.numeric(vetor[1])
teste

numerico <- as.numeric(vetor)
numerico


e <- matrix(ncol=2, nrow=2, data= 1:4)

e[2,1]             #2a linha 1 coluna

e[2, ]             #2a linha completa

e[,2]              #2a coluna

e[,1:2]            #1 e 2 coluna

e[1:2, 1]          #1 e 2 linha, 1a coluna

as.data.frame(e)   #converte uma matriz para um dataframe

i <- list(2,3,"c","d", FALSE,2+3i, 4+2i)

class(i)

i[1]
class(i[1])

library(dslabs)
data(murders)
sort(murders$total)

x <- c(31,4,15,92,65)
x
sort(x)
index <- order(x)    #mostra a sequencia de indexes em ordem crescente
index

x[index]             #mesma coisa que o sort

murders$state[1:10]
murders$abb[1:10]

index <- order(murders$total)
murders$state[index]

max(murders$total)
i_max <- which.max(murders$total)   #atribui o indice do elemento com o maior total a variável i_max
i_max
murders$state[i_max]

i_min <- which.min(murders$total)   #atribui o indice do elemento com o maior total a variável i_min
murders$state[i_min]
murders


i_max <- which.max(murders$total/murders$population)
murders$state[i_max]

x <- c(31,4,15,92,65)
x
rank(x)


#original  sort  order  rank
#  31       04    02    03
#  04       15    03    01 
#  15       31    01    02
#  92       65    05    05
#  65       92    04    04


#order > index levando em consideração o sort / no vetor original, qual a posição do 1o elemento após a ordenação(sort)
#rank  > index levando em consideração a sequencia original / nao muda a ordem só diz a classificação. / mostra a posição dos elementos
#do vetor orignal / ex: o 31 é o 3o menor


library(dslabs)
data(na_example)
str(na_example)
mean(na_example)

ind <- is.na(na_example)
class(ind)

sum(ind)

x<- c(1,2,3)
length(x)
ind <- c(FALSE,TRUE,FALSE)
x[!ind]
x[ind]


library(dslabs)
data(na_example)
ind <- is.na(na_example)
mean(na_example[!ind])


na_example[ind] = NULL

#which max mostra o indice do maior
max(murders$state[])
murders$state[which.max(murders$population)]

#max mostra o valor do maior
max(murders$population)
max(murders$state)



murders$state[which.max(murders$total/murders$population)]
murders$state[which.min(murders$total/murders$population)]



alturas <- c(69,62,66,70,70,73,67,73,67,70)

alturas * 2.54

alturas - 69

murder_rate <- murders$total/murders$population * 100000
murder_rate

x <- murders$state[order(murder_rate, decreasing=TRUE)]


city <- c("Pequim", "Lagos", "Paris", "Rio de Janeiro", "San Juan", "Toronto")

temp <- c(35,88,42,84,81,30)

temp <- 5/9 *(temp-32)
temp

city_temps <- data.frame(city, temp)
city_temps

x <- c(seq(1,100))
x

y <- 1/x^2
y
z <- sum(y)
z

data(murders)
murder_rate

#media das médias - errada
mean(murder_rate)

#media certa
mean(sum(murders$total)/ sum(murders$population) *100000)



x <- c(2,43,27,96,18)
x

sort(x)
rank(x)
order(x)

min(x)
which.min(x)

max(x)
which.max(x)

name <- c("M","A","N","O")
name

dist <- c(0.8,3.1,2.8,4.0)
dist

tempo <- c(10,30,40,50)
tempo

0.8/(10/60)
3.1/(30/60)
2.8/(40/60)
4.0/(50/60)


dist/(tempo/60)

names()

index <- murder_rate < 0.71
index


murders$state[index]

west <- murders$region == "West"
west

safe <- murder_rate <= 1
index <- safe & west
murders$state[index]

index <- which(murders$state == "Massachusetts")
index

index <- match(c("New York", "Florida", "Texas"), murders$state)
index
murders$state[index]

x <- c("a","b","c","d","e")
y <- c("a","d","f")
y %in% x

c("Boston", "Dakota", "Washington") %in% murders$state
murders$state

low <- murder_rate < 1
low

which(low == TRUE)

murders$state[which(low)]

northeast <- murders$region == "Northeast"
northeast
nordeste <- murders$state[northeast]
nordeste

nordeste %in% murders$state[which(low)]
teste <- c(which(nordeste %in% murders$state[which(low)]))

nordeste[teste]


murder_rate <- murders$total / murders$population*100000
low <- murder_rate < 1
ind <- low & murders$region == "Northeast"

murders$state[ind]


which(murder_rate < mean(murder_rate))
length(which(murder_rate < mean(murder_rate)))



murders$state[match(c("AK","MI","IA"), murders$abb)]

c("MA", "ME", "MI", "MO", "MU") %in% murders$abb

c("MA", "ME", "MI", "MO", "MU")[which(!c("MA", "ME", "MI", "MO", "MU") %in% murders$abb)]


library(dplyr) #biblioteca para trabalhar com data frames
library(dslabs)
data("murders")

murders <- mutate(murders, rate = total / population * 100000) #crai nova coluna
head(murders)

filter(murders, rate <= 0.71) #filtra a busca para os que tem rate menor ou igual a 0,71

new_table <- select(murders, state,region,rate) #faz um select indicando primeiro o data frame e depois as colunas
head(new_table)
filter(new_table, rate <= 0.71)

# pega os dados, seleciona só as colunas q vai usar e depois verifica os que tem rate menor ou igual a 0,71
murders %>% select(state, region, rate) %>% filter(rate <= 0.71) 

grades <- data.frame(names = c("Jao", "Jes", "Jo", "Ju"), exam_1 = c(95L,80L,90L,85L), exam_2 = c(90L,85L,85L,90L))
class(grades$names)
class(grades$exam_1)
class(grades$exam_2)

x <- c(88,100,83,92,94)
rank(x)
rank(-x)
-x


murders <- mutate(murders, rank = rank(-rate))
head(murders)

select(murders, state,abb)

filter(murders, rank < 6)

no_south <- filter(murders, region != "South")
nrow(no_south)

murders_nw <- filter(murders, region %in% c("Northeast", "West"))
murders_nw
nrow(murders_nw)


filter(murders_nw, rate < 1)

select((filter(murders_nw, rate < 1)), state, rate, rank)

library(dslabs)
data(murders)
my_states <- murders %>% mutate(rate = total / population * 100000, rank = rank(-rate)) %>% filter(region %in% c("North", "West") & rate < 1) %>% select(state,rate,rank)
  
my_states

x <- murders$population /10^6
y <- murders$total
plot(x,y)

murders <- mutate(murders, rate = total / population * 100000)
hist(murders$rate)

library(dslabs)
data(murders)
population_in_millions <- murders$population/10^6
total_gun_murders <- murders$total
plot(population_in_millions, total_gun_murders)

plot(log10(murders$population), total_gun_murders) #o melhor
plot(log10(population_in_millions), total_gun_murders) #o melhor

plot(population_in_millions, log10(total_gun_murders))

plot(log10(murders$population), log10(total_gun_murders))


hist(population_in_millions)


boxplot(population~region, data=murders)

murders <- mutate(murders, rate = total / population *10^6)
s <- murders %>% filter(region == "West") %>%
  summarize(minimum = min(rate), median = median(rate), maximum = max(rate))
s

library(tidyverse)

filtrado <- filter(murders, region == "West")
filtrado

min(filtrado$rate)

min(filter(murders, region == "West")$rate)

min(murders$rate[murders$region=="West"])

#install.packages("tidyverse")
library(tidyverse)

data(mpg)
str(mpg)

mpg$displ
mpg$hwy

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy))

?mpg

ggplot(data=mpg) +
  geom_point(mapping= aes(x=hwy, y=cyl))


ggplot(data=mpg) +
  geom_point(mapping= aes(x=class, y=drv))


ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy, color= class))

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy, shape=class))

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy, alpha=class))

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy, size=class))

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy), color='blue')

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy)) +
  facet_wrap(~ class, nrow=2)

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy))

ggplot(data=mpg) +
  geom_smooth(mapping= aes(x=displ, y=hwy, linetype= drv))

ggplot(data=mpg) +
  geom_smooth(mapping= aes(x=displ, y=hwy))

ggplot(data=mpg) +
  geom_point(mapping= aes(x=displ, y=hwy)) +
  geom_smooth(mapping= aes(x=displ, y=hwy))

ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + geom_point() + geom_smooth()

ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + geom_point(mapping = aes(color = class)) + geom_smooth()

ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + geom_point(mapping = aes(color = class)) + geom_smooth(data = filter(mpg, class == 'compact'))


ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + geom_point() + geom_smooth(se=FALSE)

ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + 
  geom_smooth(data = filter(mpg, drv== 'r'), se=FALSE, color="red") + 
  geom_smooth(data = filter(mpg, drv== 4), se=FALSE, color="green") +
  geom_smooth(data = filter(mpg, drv== 'f'), se=FALSE, color="blue") +
  geom_point()

ggplot(data = mpg, mapping = aes(x = displ, y=hwy, color=drv)) + 
  geom_point() +
  geom_smooth(se = FALSE)
  
ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + 
  geom_point(mapping = aes(color=drv)) +
  geom_smooth(se = FALSE)

ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) + 
  geom_point(mapping = aes(color=drv)) +
  geom_smooth(mapping= aes(linetype=drv),se = FALSE)

ggplot(data = mpg, mapping = aes(x = displ, y=hwy)) +
  geom_point(size=4, color="white") +
  geom_point(aes(color=drv))
