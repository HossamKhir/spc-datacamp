#! /usr/bin/python3
"""
"""
import pandas as pd
from load_movies import taglines, toy_story

if __name__ == "__main__":
    # Merge the toy_story and taglines tables with a left join
    toystory_tag = toy_story.merge(taglines, on=["id"], how="left")

    # Print the rows and shape of toystory_tag
    print(toystory_tag)
    print(toystory_tag.shape)

    # Merge the toy_story and taglines tables with a inner join
    toystory_tag = toy_story.merge(taglines, on=["id"], how="inner")

    # Print the rows and shape of toystory_tag
    print(toystory_tag)
    print(toystory_tag.shape)
