
library(dplyr)
df <- read.csv("income-share-top-1-before-tax-wid-extrapolations.csv") %>%
  filter(Entity =="France") %>%
  rename(Top_1_pretax=Top.1....Share..Pretax...Extrapolated.) %>%
  select(c("Entity",  "Year", "Top_1_pretax"))


write.csv(df,"top_1_france.csv")