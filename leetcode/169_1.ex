# https://leetcode.com/problems/majority-element
# 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# This solution uses Enum.reduce which creates a map with the count of all elements
# The result gets passed to Enum.max_by which searches for the maximum value
# Finally, it returns the key.

defmodule Solution do
  @spec majority_element(nums :: [integer]) :: integer
  def majority_element(nums) do
    nums
    |> Enum.reduce(%{}, fn
      (value, acc) ->
        # Update the map with the incremented count
        Map.update(acc, value, 1, fn (x) -> x + 1 end)
    end)
    |> Enum.max_by(fn {_, value} -> value end)
    |> elem(0)
  end
end

Solution.majority_element([2,2,1,1,1,2,2])
#Solution.majority_element([2])
#|> IO.inspect()
|> IO.puts()
