import tqdm

def clean_it():
	is_before_locktables = True
	count = 0

	with open('fiction.sql', 'r', encoding='latin-1') as fin:
		with open('fiction_clean.sql', 'w', encoding='latin-1') as fout:
			for l in tqdm.tqdm(fin.readlines()):
				count += 1
			
				# state manage
				if is_before_locktables and 'LOCK TABLES' in l:
					is_before_locktables = False

				# do changes
				if is_before_locktables:
					if 'KEY' in l and 'language' in l.lower():
						continue

					if 'FULLTEXT KEY' in l:
						continue

					# remove trailing comma
					if 'UNIQUE KEY `MD5UNIQUE` (`MD5`) USING BTREE,' in l:
						l = l.replace(',', '')

					# fix db version
					l = l.replace('ENGINE=MyISAM', '')

				# write
				fout.write(l)

if __name__ == '__main__':
	clean_it()
