import pandas as pd
import statistics
import csv

df = pd.read_csv("StudentsPerformance.csv")
readinglist = df["reading score"].to_list()
readingmean = statistics.mean(readinglist)
readingmedian = statistics.median(readinglist)
readingmode = statistics.mode(readinglist)
readingstddeviation = statistics.stdev(readinglist)

print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(readingmean, readingmedian, readingmode))

reading_1st_stddev_start, reading_1st_stddev_end = readingmean-readingstddeviation, readingmean+readingstddeviation
reading_2nd_stddev_start, reading_2nd_stddev_end = readingmean - (2 * readingstddeviation), readingmean + (2 * readingstddeviation)
reading_3rd_stddev_start, reading_3rd_stddev_end = readingmean - (3 * readingstddeviation),readingmean + (3 * readingstddeviation)

reading_list_of_data_within_1_std_deviation = [result for result in readinglist if result > reading_1st_stddev_start and result < reading_1st_stddev_end]
reading_list_of_data_within_2_std_deviation = [result for result in readinglist if result > reading_2nd_stddev_start and result < reading_2nd_stddev_end]
reading_list_of_data_within_3_std_deviation = [result for result in readinglist if result > reading_3rd_stddev_start and result < reading_3rd_stddev_end]


print("{}% of data for reading lies within 1 standard deviation".format(len(reading_list_of_data_within_1_std_deviation)*100.0/len(readinglist)))
print("{}% of data for reading lies within 2 standard deviation".format(len(reading_list_of_data_within_2_std_deviation)*100.0/len(readinglist)))
print("{}% of data for reading lies within 3 standard deviation".format(len(reading_list_of_data_within_3_std_deviation)*100.0/len(readinglist)))