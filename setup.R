install.packages('devtools')

library(devtools)
install.packages("https://cran.r-project.org/src/contrib/Archive/mvtnorm/mvtnorm_1.0-8.tar.gz", repos=NULL)

# install GSAR
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install(version = "3.17")
BiocManager::install("GSAR")

# install WassersteinGoF
install_github("gmordant/WassersteinGoF", ref = "main")
