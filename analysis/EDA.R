library(dplyr)
library(ggplot2)


# connect to sqlite database containing the tweets
conn <- DBI::dbConnect(RSQLite::SQLite(), "data/tweets.db")

tbl(conn, 'tweets')

