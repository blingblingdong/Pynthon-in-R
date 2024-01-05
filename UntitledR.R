install.packages("rvest")
library(rvest)

url <- "https://dhl.lib.nccu.edu.tw"
page <- read_html(url)

image_nodes <- html_nodes(page, "img")
image_urls <- html_attr(image_nodes, "src")

class(image_urls)

image_list <- c(image_urls[1:10])

x <- unlist(image_list)

#轉換為對路徑
x <- lapply(x, function(x) paste0("https://dhl.lib.nccu.edu.tw", x))

download_image <- function(url, name) {
  filepath <- paste0("image/", name, ".jpg")
  download.file(url, filepath, mode = "wb")
  return(filepath)
}


for (i in 1:length(image_list)) {
  download_image(unlist(image_list[i]), i)
}

