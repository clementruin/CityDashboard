cities = read.csv("cities2014.csv")
cities = cities[-c(7),]
cities$Ratio_Resultat_2014 = NULL
cities = na.omit(cities)

ggplot(cities, aes(x=log(budget_2014), y=Cout_personnel_hab_2014)) + geom_point(aes(col=partis.2014_Droite))

cities$partis.2014_Droite = factor(cities$partis.2014_Droite)
cities$partis.2014_Centre = factor(cities$partis.2014_Centre)
cities$partis.2014_Gauche = factor(cities$partis.2014_Gauche)
cities$partis.2014_Indefini = factor(cities$partis.2014_Indefini)
cities$partis.2014 = as.numeric(cities$partis.2014_Indefini) + 2*as.numeric(cities$partis.2014_Centre) + 3*as.numeric(cities$partis.2014_Droite) + 4*as.numeric(cities$partis.2014_Gauche) - 10
cities$partis.2014 = factor(cities$partis.2014)
cities$partis.2014 = factor(cities$partis.2014, levels=c(1,2,3,4), labels=c("Indefini", "Centre", "Droite", "Gauche"))

log10_minor_break = function (...){
  function(x) {
    minx         = floor(min(log10(x), na.rm=T))-1;
    maxx         = ceiling(max(log10(x), na.rm=T))+1;
    n_major      = maxx-minx+1;
    major_breaks = seq(minx, maxx, by=1)
    minor_breaks = 
      rep(log10(seq(1, 9, by=1)), times = n_major)+
      rep(major_breaks, each = 9)
    return(10^(minor_breaks))
  }
}

# Ville de petit budget sont apolitisées
ggplot(cities, aes(x=budget_2014, fill=partis.2014)) + scale_x_continuous(trans='log1p', breaks=c(5e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9))+ geom_density(alpha=.1, aes(col=partis.2014)) + scale_color_manual(values = c("Indefini" = "#999999", "Centre" = "#E69F00", "Droite" = "#000099", "Gauche" = "#CC0000")) + labs(title='Partis des villes en fonction du budget (2014)', x='budget (échelle Log)', y='Densité') + scale_fill_manual(values = c("Indefini" = "#999999", "Centre" = "#E69F00", "Droite" = "#000099", "Gauche" = "#CC0000")) + theme_bw()

#Budget vs Pop, limite entre les villes apolotisées et les autres
ggplot(cities[cities$Pop2014 > 9,], aes(x=Pop2014, y=budget_2014)) + geom_point(aes(col=partis.2014)) + labs(title='Population VS Budget (2014)', x='Population 2014 (échelle Log)', y='Budget 2014 (échelle Log)') + scale_color_manual(values = c("Indefini" = "#999999", "Centre" = "#E69F00", "Droite" = "#000099", "Gauche" = "#CC0000")) + scale_y_continuous(trans='log1p', breaks=c(5e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9)) + scale_x_continuous(trans="log1p", breaks=c(10,30,100,300, 1000, 3000, 10000,30000, 100000), minor_breaks = waiver())

# Partis insignifiant pour les investissements
ggplot(cities, aes(x=budget_2014, y=Ratio_investissement_2014)) + scale_x_continuous(trans='log1p', breaks=c(5e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9)) + geom_point(aes(col=partis.2014)) + labs(title='Part du budget dédié aux investissements en 2014', x='Budget 2014 (échelle Log)', y='Ratio Investissment / Budget') + scale_color_manual(values = c("Indefini" = "#999999", "Centre" = "#E69F00", "Droite" = "#000099", "Gauche" = "#CC0000"))

# Impots par habitant augementent dans les grandes villes
ggplot(cities[cities$Impot_hab_2014 < 2000 & cities$Impot_hab_2014 > 0 & cities$Pop2014 > 0,], aes(x=Pop2014, y=Impot_hab_2014)) + scale_x_continuous(trans="log1p", breaks=c(10,30,100,300, 1000, 3000, 10000,30000, 100000), minor_breaks = waiver()) +geom_point(aes(col=partis.2014)) + labs(title='Impots par habitant en 2014', x='Population 2014 (échelle Log)', y='Impots par habitant (€)') + scale_color_manual(values = c("Indefini" = "#999999", "Centre" = "#E69F00", "Droite" = "#000099", "Gauche" = "#CC0000"))
# Outliers :
cities[cities$Impot_hab_2014 > 2000 | cities$Impot_hab_2014 < 0,]
