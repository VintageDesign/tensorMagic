from pyensae.languages import r2python

r ="""getTCPGraph <- function(data,hour=11){   newdata <- data[data$Protocol==6,]      Time <- floor((newdata$Time-3600*24*(day-1))/(3600))         newdata2 <- unique(newdata[Time==hour,c(3:4)])            simplify(graph_from_data_frame(newdata2))            }"""


print(r2python(r, pep8=True))
