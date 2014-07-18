#!/bin/sh

fab mytask # this should call mytask two times, one for each hosts entry
fab -H localhost mytask # this should call mytask just once
