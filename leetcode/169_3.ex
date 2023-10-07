# https://leetcode.com/problems/majority-element
# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# This solution uses Enum.reduce_while which creates a map with the count of all elements
# When an element with a count greater than ⌊n / 2⌋ is found, it halts and returns the element.

defmodule Solution do

  @spec majority_element(nums :: [integer]) :: integer
  def majority_element([element]) do
    element
  end


  def majority_element(nums) do
    target = div(length(nums), 2) # integer division

    Enum.reduce_while(nums, %{}, fn
      (value, map) ->
        case Map.get(map, value) do
          nil -> {:cont, Map.put(map, value, 1)}
          count ->
            new_count = count + 1
            if new_count > target do
              {:halt, value}
            else
              {:cont, Map.put(map, value, new_count)}
            end
        end
    end)
  end
end

Solution.majority_element([2,2,1,1,1,2,2])
#Solution.majority_element([2])
#|> IO.inspect()
|> IO.puts()
