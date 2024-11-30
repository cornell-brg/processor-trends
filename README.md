==========================================================================
Processor Trends Data
==========================================================================
Author : Christopher Batten (cbatten@cornell.edu)
Date   : January 25, 2015

The early version of this data originated from the following researchers
at Stanford: Mark Horowitz, Francois Labonte, Ofer Shacham, Kunle
Olukotun, and Lance Hammond. The original data is in the Excel worksheet
named 'data/processor-trends-original.xls'. This worksheet was passed
along to me via John Shalf at Lawrence Berkeley National Labs around
2010. It is my understanding that John had permission to use the data for
some of his analysis. I tried contacting Kunle Olukotun directly via
email to verify that it would be okay for me to use this data, but I
never heard back from him.

I have not changed the Excel worksheet. Instead I created my own Google
spreadsheet and added some additional data points. I also independently
verified all of the data on the Intel parts by consulting publicly
available datasheets, press releases, enthusiast websites, and the
results on www.spec.org. For some of the really early Intel parts and the
later Intel parts I calculated the power by looking at the original data
sheets and finding the typical core supply current and multiplying that
by the typical core supply voltage. I couldn't find datasheets for some
of the Pentium parts so those I found the typical or maximum power on
this website (http://users.erols.com/chare/main.htm) which supposedly is
also from data sheets. I multiplied max power by an (arbitrary) 0.75
factor to have all the power numbers roughly correspond to typical power.
Transistor and frequency numbers for Intel parts come from Intel
websites. Ultimately, this resulted in some corrections and updates as
compared to the original Stanford Excel spreadsheet. The non-Intel
numbers come directly from the Stanford Excel spreadsheet except for a
few minor additions.

In 2014, I added more data from 2010-2014 for Intel processors. All of
the performance data came directly from www.spec.org. The spreadsheet I
downloaded and trimmed is in data/cint2006-results-trim.csv. I exported
the Google spreadsheet in CSV format to the files named
'data/processor-trends.csv'.

For "single thread performance" I took the same approach the Stanford
Excel spreadsheet used in normalizing all SPECint numbers to SPECint
2006. This requires an extremely fuzzy fudge factor. The Stanford guys
did this by creating a conversion factor based on all the processors that
have SPEC results for multiple versions of SPECint. I copied these
conversion factors into my Google spreadsheet and they are located at the
very top of each SPEC column (S92, S95, S00, S06). Some parts were before
SPEC92. For those I used bogus MIPS numbers calculated from the Intel
datasheets. It doesn't really matter though - since I didn't up putting
them on my final plot. As I mentioned above, I verified all the SPEC
numbers for the Intel parts from the SPEC website.

One of the problems with SPEC though is that the most recent SPEC results
(later Core 2 Duo results) include automatic parallelization. You can
tell if a SPEC result includes auto parallelization because it will say
"Auto Parallel: Yes" (for example,
http://www.spec.org/cpu2006/results/res2008q4/cpu2006-20081024-05711.txt).
This means they use flags like -Qparallel -Qpar-runtime-control for all
the C benchmarks. I'm not sure what these do, but I was doing some
reading online and it sounded like auto-parallelization can make a pretty
big difference. So I debated whether or not to include SPEC results with
auto-parallelization. Ultimately I decided to go ahead, but since this
flag is almost always on for the most recent SPEC results.

They way I generated the plot is that I first created a separate "export"
sheet in the Google doc. This includes six columns for the year
(expressed as the number of years including the month as a fractional
part of a year), number of transistors (in millions), frequency (in
megahertz), power (watts), scaled performance (normalized SPEC 2006
number), and the number of cores. Then I exported this file as CSV and
cut-and-paste the data into the Python script named
'py/plot-processor-trends.py'. The Python script uses matplotlib to plot
the data. I normalized the SPECint numbers to a 286 so that it showed up
nicely on the unified plot without too much overlap with the other data
points. I ended up plotting the transistors in thousands, frequency and
MHz, power in Watts - on a log plot this made all the trend lines
relatively distinct.

The Python script generates a PDF which I then imported into Inkscape for
some hacking: adding the trend lines, die photos, breaking the slide into
various parts so that first I show transistors, single thread
performance, frequency, power - and then overlay the number of cores and
parallel application performance projection. I removed SPECint data from
before 1990 since they cluttered up the plot, didn't add much to the
point of the slide, and weren't really for SPECint anyways. You can find
the SVG in 'svg/processor-trends.svg' and a PDF of the plot in
'svg/processor-trends.pdf'.

