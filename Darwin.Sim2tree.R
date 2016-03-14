#### TO DO:
## Add year of publication
## Full title
## Some kind of bootstraping?
## Number of words (size of book)
## Remove headers for PG files

 
#sim <- read.delim("/Users/pjulien/Dropbox/Code/text_phylo/Results/Darwin.Cosine.Sim.lsi.Matrix.txt", row.names=1)
sim <- read.delim("/Users/philippejulien/Dropbox/Code/text_phylo/Results/Darwin.Cosine.Sim.lsi.Matrix.txt", row.names=1)

info <- read.delim("/Users/philippejulien/Dropbox/Code/text_phylo/Darwin_book_info.txt", row.names=1, header=FALSE)
colnames(info) <- c("Title" ,"Year")

dist <- 1 - sim
sim2 <- sim
diag(sim2) <- NA
 
 
 
##### Heatmaps
library(pheatmap)
library(gplots)
library(RColorBrewer)
 
pheatmap(sim)
pheatmap(sim2)
pheatmap(dist)

sim_title <- sim
colnames(sim_title) <- info[colnames(sim_title), "Title"]
rownames(sim_title) <- info[rownames(sim_title), "Title"]

#(This one looks good)
pheatmap(sim_title, clustering_distance_rows="correlation", clustering_distance_cols="correlation", clustering_method="average", fontsize_row=5, fontsize_col=5)

# Alternative color scheme
pal <- brewer.pal(3, "Set1")

colscale <- colorpanel(n=100, low=pal[1], hi=pal[2])
colscale <- colorpanel(n=100, low="gray80", hi="firebrick2")


pheatmap(sim_title, color=colscale, clustering_distance_rows="correlation", clustering_distance_cols="correlation", clustering_method="average", fontsize_row=5, fontsize_col=5)


#### Trees

library(ape)

tr <- nj(as.matrix(dist))

plot(tr, type="unrooted")
plot(tr, type="radial")
plot(tr, type="cladogram")

tr2 <- tr
tr2$tip.label <- as.character(info[tr2$tip.label,"Title"])

plot(tr, type="phylogram", edge.width=3, edge.color="gray30")
par(mar=c(1,1,1,1))
plot(tr2, type="phylogram", edge.width=3, edge.color="gray30")


### Attempt with heatmap.2 in order to have heatmap * NJ "clustering"

heatmap.2(as.matrix(dist), hclustfun=nj)

#### Per book plot


book = "OriginofSpecies"
book <- "FoundationsOriginSpecies"

v <- sim[book,-which(colnames(sim)==book)]
v2 <- as.numeric(v)
names(v2) <- names(v)
v2 <- sort(v2, decreasing=TRUE)

barplot(v2, border=NA, col="dodgerblue2", las=3, cex.names=0.7)
