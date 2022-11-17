
all: curso

curso:
	(cd md/ && make)

.PHONY: all curso
