BEGIN {
	maxsignal = -200.00
	maxbssid = "NOTFOUND"
	maxssid = "NOTFOUND"
	maxdata = "NOTFOUND"
	maxfreq = "NOTFOUND"
	}

/^BSS/ {
#	print $0
	bssid = substr( $2, 0, 17 )
	}

/signal/ {
#	print $0
	signal = strtonum($2)
}

/freq/ {
	freq = strtonum($2)
}

/SSID:/ {
	ssid = $2
}

/OUI/ {
	# Check 15118
	if( substr( $4, 0, 8 ) == "70:b3:d5" ) {
		# Check Compatible ETT
		if (and(int($9), int(ETT)) != 0) {
			# Update values by maximum signal
			if( maxsignal < signal ) {
				maxsignal = signal
				maxbssid = bssid
				maxssid = ssid
				maxfreq = freq
				maxdata = substr($0, index($0, "data: ") + 6 )
			}
		}
	}
}

END {
	print maxbssid "," maxssid "," maxsignal "," maxfreq ",dd 25 70 b3 d5" maxdata
}
