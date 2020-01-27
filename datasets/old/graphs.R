library(igraph)

getData <- function(day=3,datadir="./Flow",outdir=NULL)
{
   x <- ifelse(day<10,"0","")
   ## This takes a long time. You should save the data
   flows <- read.csv(bzfile(paste0(datadir,"/netflow_day-",x,
					day,".bz2")),
				header=FALSE,
				col.names=c("Time","Duration","SrcDevice","DstDevice","Protocol",
							  "SrcPort","DstPort","SrcPackets","DstPackets",
							  "SrcBytes","DstBytes"))
   if(!is.null(outdir)){
      save(flows,file=paste0(outdir,"/netflow_day-",x,day,".RData"))
   }
   invisible(flows)
}

getTCPGraph <- function(data,hour=11)
{
   newdata <- data[data$Protocol==6,]
   Time <- floor((newdata$Time-3600*24*(day-1))/(3600))
   newdata2 <- unique(newdata[Time==hour,c(3:4)])
   simplify(graph_from_data_frame(newdata2))
}

