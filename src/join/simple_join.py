from pyspark import SparkContext, SparkConf

if __name__ == "__main__":
    conf = SparkConf().setAppName("JoinOperations").setMaster("local[1]")
    sc = SparkContext(conf = conf)
    
    ages = sc.parallelize([("Tom", 29), ("John", 22)])
    addresses = sc.parallelize([("James", "USA"), ("John", "UK")])

    join = ages.join(addresses)
    join.coalesce(1, shuffle=True).saveAsTextFile("out/age_address_join.txt")

    leftOuterJoin = ages.leftOuterJoin(addresses)
    leftOuterJoin.coalesce(1, shuffle=True).saveAsTextFile("out/age_address_left_out_join.txt")

    rightOuterJoin = ages.rightOuterJoin(addresses)
    rightOuterJoin.coalesce(1, shuffle=True).saveAsTextFile("out/age_address_right_out_join.txt")

    fullOuterJoin = ages.fullOuterJoin(addresses)
    fullOuterJoin.coalesce(1, shuffle=True).saveAsTextFile("out/age_address_full_out_join.txt")
