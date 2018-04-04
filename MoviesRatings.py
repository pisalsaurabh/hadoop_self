from mrjob.job import MRJob
from mrjob.step import MRStep

class MoviesRatings(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings),
            MRStep(reducer=self.reducer_sort_output)  #another reducer
        ]

    def mapper_get_ratings(self, _, line):
        (userID, movieID, rating, timestamp) = line.split('\t')
        yield movieID, 1

    def reducer_count_ratings(self, key, values):
        yield str(sum(values)).zfill(5),key      #convert the value to string and then add 00000 to left of it
        # the key is always a list so we are itterating throught the list in below reducer.. and zfill makes t sorted
        
     # Pass this reducer output to this below reducer   
    def reducer_sort_output(self,count,movies):
        for pointer in movies:  #movies is list
            yield pointer,count

if __name__ == '__main__':
    MoviesRatings.run()

