#!/usr/bin/env ruby

# Get the string argument from the command line
str = ARGV[0]

# Use a regular expression to match "hbn", "hbtn", "hbttn", "hbtttn", "hbttttn", "hbtttttn", or "hbttttttn"
matches = str.scan(/hbt{2,5}n/)

# Print all matches found
matches.each do |match|
  puts match
end
