# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJzsvQl0XMd1INobutFYCHAHF4CPBEECBLrR+0KQFBs7CDQAAo2tSRBs4D0ADfYCvW5waTVkylFsyaZtKlFiyJZjSCPFpEPHdGLHVEaayIti2bHjfkzrCP/54I/H//jP55z5GSq2J/qY83/+vW/rDQBBUU48/wvovnXr1q1bVbfqVd+qd1+9/02W9lcmhL8KbZPJPi8jZV6ZVkbKSUVA7pVzocKr4EKlV8mFKq+KC/O8eVyo9qq5UOPVcGG+N58LtV4tFxZ4CyBUBrQeXm6htxBCVaAoWOzdJEdaXqAwWOItTcNL5LKQrVJGbT4oo/VymUJGbSHVfyqXyf5MLlaco8pntopxUvOA9Pzs9BFZSHVJdlk5IrskF9q8zbsttKcyN682O6/IDTKUvISsHAXZObQoUzGzXeIozOSY2SFi3p3AWUYWkcV/qgAOhUhf3CVb5Y/anV1SqBw0twc0t927l9PcptyWkwrv3jN7Q/l8eEku6kEouSSr5PLVSv5T+P6ZFFuseDCPd/eUzLsvRxOla2liQzIJimiWje707qf2LR5YjZ/an93+a2UhTSU/AoTeg3pV5tRr8yPV6yB1kKtXFVW5Rr2qHlwvqJF65pDIMSUjt7wsz8zlPQx1rwa+GnJrZgqU/hnvQXKb90iOlO05UmrJHcBVRx3OpH9R9iWFV0fu9Oo5GfWSbsrIXZljxGsgd3uNWVx7yL1ZXKYsjnKyIovDTO7zWqgjX5SRBFULcD+lA3iA0n9RRhkAq6SMHDRx0MzxWaCepV4rVb2Gpq05mv7sGhp73WsjD25QY1VeXQ7foRw+e1aLD5PVWS3euwEpDrLmX7UPjuT2AWWH7174OjbUH1u9zjX7w5nTH2/AKD66ep9cl4/KvQ1Q42NS/Y5vQGMnHqj3x8haHPPwPU7WkbrM1OzrgNRz18eJbDpHfWxVag4vWS+VZyCNDyjPJPGaScsDeCslXitpeACvLa0O9g3XQU46NlyHB/M6YXQQ1NE1RgeRPTquy68pYXycXOOa/d+9rszRQR6V6tJAHntAXYiH4D0u8R4m6x7AeyJNz49tWM8nH6KvDdnXbQ6v69++Dl/aAr+EJ9fo6YM588B/XufXbK25uXGVubnpo7n5w5ubyWZfI9SrYKZJqlcL2XqrLctKbF5NHtmeKW+xZVWuDrI5q52tWSWe+q2X2JZVYudvvcR2ssvbwdmd6eW6P3C5p1bl6s7kIuWphcSGa9oZ0qJlSvZ4OzOs0/R69/7W9dWVVeLp33qJbqrN2021enuySu77kEvuJvuzpG20hr2kJ6tuA79trcSQOogwq+Shf42Svaf/ta8Ybycp9/ZRnfAbpPEaqT7ycKwYqH3X8slhbz/VT45c4MqlR/9nuJKjT6fSqU5sia8x9FlohVdoRfxffUY6/KG144iw97HDuxfnqtV4pN2Pbdm7H2vlWG3uo1qpNqqd6qC6KJgjqB6qlzpNnnmxwOvJ2gk6m7N3NPq0zDsAds4gec47RI55h8nz3hHS5/WS494z5IT3LEl6R0nKe46c9I6RU97z5LTXR/q94+SMd4K84CXJgJcig95JMuSdIsPeaXIWJPrJxwHOkHLfhSmZLwDyg/ANwTcM31lxxwpCOvB4kPbSUJMI5IiQ0GRvlJwDOAd1n8ncxwCui5BykbwE8BJ5GeBl8grAK2QMYIx8AuATZBxgnJz3zpNPAvYk+TGAHyOvArwKMi/myFT0y2qeqlHFdk6Eg/pJ3wQ1Hg5f0PvISNAX8k1RdGxzRkLAH6WySGF6wreyNYN0wReF3PewiO4aOSs/AmCLZ5qmfGRvOBxouUxNzEXDNFCLGynfXNQ/ORfoD8/NxogCoiMUifoCAX9oigj6IxEuDJNzASpC6PX6WP2sf5bw8zwETT0+R0WiEWI8YiEm56JzNBU5ftxEnCDqSepifWguEFgpnb0SnQ6HCPfc1LQvoJ+9EtuSLmL2ysQcHYg5L5NTuvAsFSKmo9HZyNH6+olpX1R/CUDENzurh+bVN0ctl1oGmy95PT3NodORixMz4xFTR+ykmIP2XdJP+aPTc+NzEYqeCIeiVCjK5YzSUV2rn6bqSVBMfdDnD9XP0uHLfiqij16OxgrTIqz80lwt6G3PGWOD0xQ884tnvjBK9Ha1uPpbiCFXh4doam9p6uzobiMGeptdnhbQCSunP2AlIlEa9MtXouEDSZjzYebqebisVjRtHp3RYLQKiMkgIGYJEZMsIsUiUqwCxSQmWSQEkvIRcRidImaymVa0iDkNNkMHT3QaHCYJMwsYCBYxq5hqdIqY2SAIdFoNfEVMBoGEiEEkRTjEjBQs1WK0DPf0cjSb0+jgELvBaBAQk4iYRcQiIkIr7UaDhFgFRMxuEikmI18TO6ikTyAJ6rKbDWYBEbOZTRIi8phsAiIWbzFYY6WIWK0GrRUQh0EozIG1z0PEuKLmAj6LQ6yfwyjUxmEyGfp5kkVg4tTII1AJNYe0ccwurqEcBho2rBQg1t3c19PRzFEbTXZBbKPVbOaVy2GNKbRrZZOIejtdHd0DAr9Vymk1mgTMbhIwu5RqT9EcIg3GgoiZHQ4OazIbhNQmszi4msyg3T6BaDamiKY+CTV7xHSTlG4y+QWi1WQQiIB1iERh+CFmFTC7MHSbbHahnBajyWHihbcYrYIWW0D5KcwkYlaJZhVpNmGoAmY1DfFEsziiWkCXTj4ZsY4UyhfYZjUb2mOITTkNhkmeBr3cymHtTrE6HTCOHAIGI4jHbBahlA4HqnkTj9kMPZ1dnl5XKu4d6vJ4PAKnyergKtGBV3ZzTCDaHAKGVyefEWrW6HI1egbS411N7T0ZcRTMi4MatnBC/A67WGuHXbgMO5yClhBxdPF8TrxaBaLD0CKhpia+CERbhriBKCX5BRRGe5vABWhXJ1TMk0pyp9DeFOqRMlgH4NpolDKYHC0ptCOFDoqo1dGbQiWqLcXrNKVQa3sK7eL14MSBwxNhPumQUGu3hEqyoAfaUuiwhNoHBVkw4GKo06A4SbutNqtA8od4BXXDwIHJI59DxZkBMauIGSWacOV0Q6/BbJAvoFaByOktX0BNEpZKtqaSHRLRwc863Q5xku/mJkABM0o0k4A5JT6nOAJ7oWRD05BruN/FieXi7hTKFwuoka9/L0whQv0RtUqYQ8SEYnslhfRa8SIv5DGjYbjZKJKFevXaTMK45bAuiWgUMaPEaBRpDlG6NCX32s2iGMQaRaJRSjaJydBvzSnUHZPQvhQ6GMsXUKOIGXms3wxTi4SZJMwsYnYx1Wp0iBjQtBwGA8svEHFACUSreUhA7XZDZwp1Cyg0d0jIBf0pYlahIFQlz4hYn0Q0iZhZSjYbhiTU7OHQCKKXRNaUTCvfIEi2STRHCjOJchzmRpHoFEuEDhCSAeuSiEaJaGxMoal0k0Q0NUpEs0SUCoJOFYlGQ2MKbUqhLSm0LYV2pNCuFOpOod1SCVJdjKZUCaZUCSap2uJosELnism2VLVsqaJsBo/EapYwu4Q5RcwhCXIYmgUiDEoRk8oBzC+idqlIQDtSqFhPq10YjVabJMlmEKthk1QKWKdENIqYScpilxixxE0i2t7Z6PW4RCanxOSUBqRDGoaANafQthTqT6FdKdSdQj0pdFBCjX6pBIdEdApEG8xdfC0Ra2zEX1spRehkxISxBa0XiUaD2PM2k1O4WPpt3IjbJKLeIZe7Q+ghmzRobGhJiUSrcFHYrOJFgVhzChU6yGYXlYZYVwrtllBxzOH0J9QBsPZO13CrS0oRi3OIPYpYYwptSaFdKdQtygO0ERZnfamkXkmgSSKaUgLFawJRv8TqkIgOoaPsMPm0SKhZQq3iCLeDsSRi4iBDrEsimiSiWCigoqYBdUhEh9DHdrOoVMTaUmiXlG6SiKJ6cf7n1YGYix8y6XEwa9LjHk9XbyoOP6eYrhXjXSlUrKl0ASPmlogmiSg1D1B/CpXqZ7NJmENKdnSIRElRYMe2SKikKKtjWMTEGdtuF0cLYmI5DqcoHTBBukOah9A6FTCbOLQ9sBpxcmaSx2gxCAj8puAyatDhE0J+mAw2icNk0A25+jnuIaPZKCDwA4TIsEOgDDskit0gIE6+BiNoBPtLD8tksQp3OOYPBHz1Vr2BqO7yh+YuNxADDYQrRNJhP1mTz8ptrNzOyh2s3MkqjAb4GuFrgi9MhgQV0s1FGoiY3jU7G6CGqPFOf7TearbrzTaiurPd4+6qIwL+CxTRRk1cCNcQTdN0OEjV3+uQyWT3SACs3OCfLpXJ/Ae3AqUayX8MILbNHR73Byii3zfpo/2CyBU5EVNAaYoaYkWujx1YrfJCzQmb3qA3NsTsQg2NhgYC7FJeaPCKJzw3MU2Y24j+gJ+kiMY5f4Csb+vrsBhqOowWx2BNzW5W7mLljay8iZU3s/IWVt7KyttYeTsr72Dlp1h5JyvvYuVuVt7NyntYeS8rP83K+1h5Pyv3sPIBVj7IyodY+TArH2Hl3nu49XjvPyuhaUcfTlcOJ7TEYobA6YxtzVaLWW/M6sQhf4gMX4oQ3R5otB6afU+LRReiVosbCEi2WRqIyzZLTay6hthYXe5NoIg/QhFKqI3/+c3QY5/EHqtEWr7Ur19HvjykbcrsulhVRiXdvgl/KBqOTDcQHaEoFSCAQPT0E/c0KKCEGxhjMcNG6yeV/wPI6f8y5I9tzSyf6Ontq6/R0G8BA/23CJCVfhvBDxH8CMHfYc1rH2LIsLIYMUVFZ+nwLEGH9eNI1F+k6Ig/HNLTVIDyRShPjZzNi0xTgcBK3lx0UudYkRfEytJyQUjOTUT1wTBJBWJbc+T5STaPCo21NcZ2i2lTkaA+PEvRvmiY1vsCs9O+FXkdq/KGQ1OxfauJ9oXmJn0TuEdKr1r2OO0LkbGKVVImZuf0PtCBPxJdkR+NbXuCpEIRf/TKcZPeUDdN+aemo8djh9MyTl+a8+uj1OXoWMBHT1FjE76JaWqM54xp6i75yej08dihB+bgGGsUrNzIyk20Ei4gWgWgpoAt8fEX+ZigaTaPUx2bx+mLVU2OByYQBicRjnMU8iLCCAcnfBwluGLK2fi9dOlSaieb2/b0BcOoYzoy7SP1VttE+g0RNXzhkpb9alCGfrtReSopqkzhM9L9Etz/X89TY15GKuP8nT0Vwn5ZTV43/fc4qq8DU6zsTGujq7u+h57w6YSZrgEog/WxBFyXBr3JrjcZLUBqHKy3mMCesDvNNoh2NdVzIwjQPkxxmOw2mw0Zm/rqu6lZX4DwwGiFBgPJ3Vrf1daCQprrA1MUIL3d9Tm7/kBuHqzvcnfC4gfw/sF6oxHCnt56DJpc9T46SMHA0V20+44KOOZx10sjyKi3W4XxYDdJg8loMZnmG0ZrlKwyEqVZNY7McJDVYAiTBlxNSno6GEGdEazSFwmz6jnfmG/WT+8A2gtAjlgBXJUtawo+Y7t2YqFyYYIpPJAsPMBoKpOayqtbl7QHF/sZbfV9mexIXPmeTFYQVwKumFf+CjshptlzxmlvMAY5xCgiJhExi4hFRKwiYkNEteeMIRgr2HPG7GiwNlhsXJKxwWkMrvCIXaCYTSJiFhGLiFhFBEQVCqJMBkdw7pIa7w8YGpzW4C8+/7lf/PGtD/L5/Oc42fbgz1977mc3f/HCSz+7Cdijif385wo4AaZgAUGMjXFfgATBoWNpMfFPRAuIOEGcrScgiHOgnssgxoCj/iwhogI/EOolfgw4fiETiDqbxR8/Wx9P54+P8ZkwXo/yz2bxC4y8RDFIqx1xliOjBOAfw6Sx+Fkk1BNcMCYQ64EAf2fHeCoQC4gP9Ffwu9vtINQZ/MXzT/3ij79NcOKMwftfeuFT8P0D+D4L36vw/Qy2QmT+/DO/ePEFgML4J9x9hMfl7unpW1Pc53gxC69D+AyxpixjkPC0uNxETyvhHmhrd3WtKfApXtjCfxAEvyHUGb+fyBFOCDXla7kR2W8QgHwcGy4IvQ7fT68h2BJsdTW1NPb0dBLtLV29eJPP29PdQqxZwmcFVXxOEPw5If7ZXL0QwoXZ2tfSQrR0n+oZWVPqc2Jf8SW88LRQ9WdXlcp3nUHvzJEHMZugB04efj9JCNX9PSRg5NNpo4QfIQLhKQKw638IXyBfvwbfzwrf54j7q40sKZ/A/jx8PwHfTwoiPo0JT2F+gQANvP57v7OXVIHuof8KCoTflDO/uPryKDHSMwCDtKO7mejo5yNEY0u/hyCGWly9Pd0fpIQM20cp2j4Hc2wfUp7jbYGWjKI7ZhWU9XDlogE9S8Nv/00ZvRPtwO0A2LyAP0RdpvcCjhZ8ZCf/o6/SJgqaGVVLUtWSED9crtVrn2u5zaR59mS3I5qXZuGpU/ga7WXzJmAJQNeoWEU4wqojVyJRKkjvxtqrAuGpML0HWyM1ia4QwY+xQfv5BuUXXNNeP8zk707m707k717OL/4M+WzhtcJnuH8uNyhI03glSkU6eibSWiJTia1ckGe3MtMXZF6+ur2axaWIKxbT+FJ/ccWMSsJlmRauXLZOLkmfcXl2Li3mU6+WL9uPJbS/UhZVpNJnNCJ2UEaXzCtJeVyJz9BMKEagZ+aVTyr7hTDldRSXL+Y/uKxF7Wo8YNNnWvEqqHnBRmoeV8E4UXbHNC00HaaPEvT/DeSaQvoADhE1757CqpoQqiNUNDwbZZUDfV2sdqivw9PS7PK4WA0sAyfDdBDWiCiDzYeF1UVfYI5i1SQY9CSFgzAcoWryWCXKKaGpyGw4FKHGxucmJymaVXGFyCk2X0yJYK9wP7D8lVYEIsfERNoMpP8FGCK4lobxuaP8Of/z/qs9vyzcfK3h2ePXjl9tXlLlf7Lz453XVc/nL1QyqoqkqiKhqkhRNy2WMCpDUmVIqAz3Vcq88qX8os8Vfaro2U3XNj0D/+8vg6xj92XyvPIUWCrZu7D5mfln5hP5e7M+78PffSXwYKiWle57t+Tw3ZLDTElNsqTm3RLD3RLD7Z1MiTNZ4rzajtU49fFTT3U93XW16+eFW6/2RPBJsu/s2ubSy76jL2ksUn7nuKpRo/yuXA74dzV5ADMuK1QPd1mZZOtNHqQCLgXg+zNp8M/DMOM7vPjMOZ8u5tJ5DTpn5Sj9P7DbFayCpmDRMzcOaJE/NDsXHeOddNhNOI+EKFKIRxRcB/G9s4umguGL1FjkSnA8HIiMwTJpLDILS7UI7YT0/4JdtZfvqu07nx9M7K27MX67jtn+WHL7Y1e7lwp3JVS7cidIaWl7Nu+3MkEqSFlANS+LFqbxp5ch5c28ZLJcFpW4SI7LFjWyVf4yc85Il/dD5JEu94fII134mAcm1p0pzniWvnBCJWGp//uKlOslUPJIdRZFRWqyKBpSlk6ZVJ2FCXheOa+az5tXR9MeUoWpqHi1WpPKLF2mScuqpSa9l+IaMj9WgI/jxvLwEVsOL4zl5srPylXEcebH1Dmc2rg2nsdpmO9PNQe5DZB4PsLFTau1IGtqLnkwz3yBVhbdn6aD4qyaFMYL4oUXZbQxfRznPrr7aKN2vgjNg4wSSuKKXA1mXk3ZD+g+VOrmR8i7Zd3UreumbstJrUxL3Z4zK+zg9TBfvMZ8szNevKqeqtK4Jaff7B/baE0aV+oB47IcaboUX47LLPQcGBv6FAeYGLvnN6W3Or7ao96y+U1PbsLcPJYyPGp2dfN2H862K/LKe2hI3cPIPRxN9H0A/l0vyGX3cNK/hy31P/Uv//IvfuZ/aGSxpgc7bg5Egn6zwVTvm6XDYBjwrpu+WT7GeX+WK/mFA79M6GwZwSWDq7e3r2ewpVkfK9+TnXw0tbdFxI4JNj1x/AP8xdqEpSLR3eNpOaojPO1Qtqenpwvr0OvqaCYKsFyi3TXYAnQgjRCtsPzmq+fqIlo7+mBVo48ZYdFptjdYjEEtLHG6mnrcHD+/TOclumAxxK1+ufVuMDYq1ry/BVIsBgPR29lHVKN4o5Vodo1IWuiqQVmuZlhPEU09vSMpVXBZpbT0mmWJt6aLNxseXbye6Oho5XTj6mshuKX9QH9LH2iwpZto7un2EL19Lf390GIPUIlYRzsVCISrTIZ+Pw1wP3x7uRsUgLi44YCY+woAT/gCFcJwmkqLdUQAHIVvbI+0Xe7TB6n6WqfJbLA4TUajxWah/xFGaE0ZvQ/HNIEA1zv0fjRV8mcDvigaq/RmjGrArqTm8PbGXMgXpFhN0DcxDYs6ViNu7GuEeyicJcMqYQnI5kVmA/4oq6ZCnHGrnIY1oJlbD3IWE9hPVyKsiroMPKqoH6TmRQIUNcvmi0Oe1bZcnqBmoyC/poR2cYuxOayFAr8XjPA1wdcMXwurhiIxTTVLU5OsKgImM6umKV8AaPmohSbfNJQZjEyxyuiFCH0ExEXwlyhr745f3/WKAHUUwQUPGGUK1dM1z7Qxim1JxbaEYtuyQvMZ1VO1T9derV1SbL5aj//L2qLP9F3zPnv22llGuzup3b1gZrQVi/lf2fTyJoYwJPHjYLSOO2V/U/HXFYyzI4mf04z2dKLP+27f+bt955m+8SR+ZhjtzNWDyxpicRujOZTUHLp6YGlT6fUt1/df33Jt8nrfgnxh/4Ly+aGFvkX54v5F5YtDi3035DcUNxSvDCY21T5Ve/XA1b5nFM+YoE7P9H1u+FPD1yeeHb02umBMFpdDpZLaiquHljUFz7Retz3rXjAyhXsX+pjCfYs7mMJqRlOT1NRg8WK6jSncz2gOJDUHrh5cKtj0DP3s4esHnj1yve9Z3YKCKdi9YGEK9r2rPXxXe5jR1iS1Ne9qdXe1OkZbn9TWXz10X7FDuXm5ZE9ir48pGU+WjIN5rym+XpbQ7ILPsrowUVTHqHVJtS6h1i0XlfyR4vmC54qeL2KKypNF5VcnltQFV8lfIpvh9hamyMyoLUm1JaG2cFm7GLU7qXYn1O7VosOMeiSpHkmoR1ZJLW5h1K1JdWtC3Yrii0OMOpxUhxPq8HJutOgYoz6eVB9PqI8vFQ8nRs4wxWeuTrwzOpYcnYTpf1reooCgVdGheA9jXHBOfkrxaz64zwfLau3T00/NPD1zdWZZXfD0zPXNTwWfDl4NLqs38VT8f39ZuwVWU8rNKbCs0j5Txa+G0v+FNZVyM4QRAsbrW4dcilMa2d8eadoDwY80BadqlT/aXHLqkPJHh/IAz1g+oLHNLR9khbh8wJNd5sGAJuX8003X82hnxo6RIudHOD1VuW6qat3UvJzUtL2IHBMh3XjJOusGTPk08z+135F75k1cTuZflF1X0fJ0QzGnrPRa5pxts+FaFmQvKcDETTP4YalQmPXM2AYWMRvZC5lXhlxgCm1JpYMpZMlqV1FOu7anUmck7WQb4sCXtoTJbn/6mUEb1nCuEZ+eWrJuaq6BvNHeyTK851Xr5lynLVOy+Tzo2T0pjvWM9KxS1cKzc8Xz6tSzcx+0JhmayTX/15OadoJRPOvqapaN1s5r4nmrL+MyFxWwmOSWAV+EJcSXlOu1XC67VvehtHPHhzYC8uP55E5YYu6JEimu1VuduzQJ7d5Arl3rLrp239qTmW6FBfi6ekhbXEUPp/D4upqfL8jQ3954AefVUL7q8i2ds+JhNB1Xwrh5CpbthYvbVtXFvkxpZxW4/J4vjufNb4qrcJamK+Laxe2r5Y3WpbW1KF4MyzqY8/9MmvdhbJ0AGcS6MvQPlHEeZOwHGeVryjA8UMbH4feV+8/eQw8VVsqMsojqkoK/5nHulGdr/MBDje30nJXr9uTBtUZO1JQmf50xxI2YKoRrSrJsXNIHvoIP5eRc3Q44nM2Hy32wBXCE/PmGZ5rqD1zPmmxfIrC3cISXRu1rS+DqKOPqWBp1PpBvP8fX8EC+Ixzf8Qfy1XJ8j63Pt54tIOi4DuRsibrW5xO/YLU0pjhnpBNYZqR58iC3YM3oF11Ov6xT2ghXjrTFo++OKY8cORIrOWMcJZr6XE2dRGtHVwsRKz1jGiX6XN3NPW6eHis+Yx6FdX5XV88Q0doY054xjBItwx0eIraVaGrv6elvIVzdRE+vp6On+yhBl8jxxgHnHccqDMZYLdE74OGFtwy73L0QHiWI+gg54aPJ+lZ/gNJfvhLTU9EJvT62M8Xc6/K0C9sVIBW3vWO7+JSuniYXFoYbNFCxge5mglvixzZhY9wtnvaeZqK7ZSi2BdsixHu6muuRtglbk6LFCsQ2HCViNUQ7tNHt6h6B0vv7h3r6mvuJ5h5uR2PI1e3htz2aiceIWL24A5Vq06SfjkSJgC8SrQM0GhGxSNRoMsc2cS0TxRIxBZR3UBLeAsL7sfCmnp7OjpZ+4uhjRPVIfXfNUaImj5Vfof+rDHcbrlARVjlCRXjfQx+qWB66h/eKbsrZwqDv8tilMH2BoiOxMqirx9VFuJqaQEEeqJ5QYfouauqAuBHEdTF6dvR7XH2elma9Xi8krcjj0I0qvhtN6PVoBsTMO4xh+m7c1yF6+3qacE+n3dUPlUdVgJSVTYQnHPUFiJ7O+qbeo8SKvH5le8bmD2iyEQcdjRNX7E8I7Lk+Ct3qiF7fBX8k6gsRE4FwyB+aKiC4IcknNvpCUwEfSUWm05LNUrJrcmraF8rObpHSO0Kk35eWYpVS2oI+fyAtBQZ5o2/iAhGkQnMxLdE0HQ5HKOgN0IMF9GBBxAqIFZT0UxmnJENsbwGMSaIDW9jd4gF9dHe3NHFDFfRac5Dfd0L3ALoTQWpDqoLb80G/T1aFxxKwBdyeEvoTRNjNeJF0h6Ot4bkQyd2WpbsxUw+XCStIt3HbTTQoh2LVvlmQQ7LK2YlZVhWlKZLf21IGqBDdjpg6Mjce9EdZ5eTkOKv0zfpZFQAjqwxfgPE1MQtg1neBVYyDEN/kFO5ykWzeFGqIdqOAfPGkA7aAEneuImxJUzgUoiYwwtWypoSVX2YVl9HbFVrAKibDUN3oNMiaReddNn82MhbwY03kflYxcZktmqBB52NC9bRRHENjfjLCqnALGeoBaB5uzEUgry8SQSlr723FRLANt8D+PA/3tu4rfHLtzvtq2Y491+VLW7ctbP+DY88dWy4rT1TUM2WGZJkhUWbgogamzJgsMybKjBBdCDNl+mSZPlGmx9gFpuxIsuxIouwIxF7QvKhZ0CzvIRL7bcwee3KPfUGxXLb7RW3iwCBTNpQsG0qUDS3tKV/cndhTy+ypXSaqXtK8olnU/JKoShzqZwhPkvAkCI9EXz5cl9B1MIdPJQ+fWlTdV+Ttr1/WGW8fvB25ee7WuXd1J+/qTjK6xqSu8V2d+67Ozeh6kroe3BB7f/mw475Mub8+BZardQl9B1N9Kll9KlF9arm67lbBbePN4lvFN4ohclN9S32D+7+vAe7333//N/my/YeEimAFbQxhTxL2BGHnokcZoiFJNCSIhtxUIVfVkRvHmCpHssqxqEpRRWSp+shi3n2Fcr9l2Wz71lzi+DRj9yftfsY8kzTP3Mi/kf/+fYV8v2XJZMYIRN9/P1cKV7iXIc4kiTMJ4kyKXqO/cfnmvlv77svk+wflPFx0LVXrvl701aJvDSQa+t92ve37YRMg/IexepJWD1M9kKweSHCfNUrrYgh3knAnCHeKXll9Yy9TaUtW2hYVS5VViZrGRCV+lqtrv17w1YLb5pslt0puwP8vMwnLVTW3xxNVTqbKmaxy3peV7Kfkd85CX93U3NLc0Cxb7G8o7zS+pnld842ub3bd0P4Se7Hz7Q5GP5AY9DJ6L1N9Jll9JlF9huvfYaZ6JFk9kqgekUQsWWz3Zfk1lJyHN5qXjp38m1N/ferNyGs9r/d8Q3tbebtlqeHk7fwls/3O0YS5BT5LjuZ3HZ13HZ0/aUr09ic8IwnvOOOYSDomEtxnyeq8401Y2+DzgVibE6c9iQFv4swE4yCTDjLhIN+/v5mrZAlqgNcDD9/j4K9l2fS1IO4NrpH0GwJG9GKAIcxJwpwgzJnd2sgQTUmiKUE08QP6W5E3zG9EXnO87vjG/DfnmUPNb/Yzh9p/svUn/e+c9vxw+MfDPyz/cTlzaJAhhpLEUIIYyhR3nCFOJIkTCeLEMnHgFW3iyDGGOJ4kjifEz1L5vsWjiXIdfNJz3pfJDneh5/d+t/LXHLzPwRTPgcM3CpkDluQBy6J8qfLgjYLFxxYfg4F2M+9W3g3uf6nq0I0ji2OLY8vVR26qbqlucP9p1NV5V6cK4wj/f5k+T2TU/+BL6lfUi9z//YhCto24fuz+rEJWoYfU93+jlpWWJUsOJEtM92UKmHUlsFy6PbHDypTakqW2RKltuXTbc+rn1deF//t5wIJ7vC/BzP7xRutAvuy7DkuTTva9Ojng39M1NNcqv1+tAPz7R+SI17qcEPnbqr1tCtkP5Mj0A4WqLV/5A3VzAUT+rrRpf/cJ5d+biiDy9ydUPQrNTxVKwH+aJ0dc3WiDCHPCVQrBP5RuQXiQgw6EySIOEpsQGhB/J984cFz5zjE5wIxNZlwWcJvMURVuMk/BkmdtF7fMhdT6nis5Dl1ybcaiL4N3/W0QRWgLLDfStlNhaZEHyxHVvGKtbcy4ImdrrGleSeat7gxHqp/O2MbK3o5uXt8XQbWWV0s8Z1v9WnN0c1o5+be0ORtJeevqf2sqLX0bOL7u0n1endFvBbx3yHqLZLIwLn8gT+7GdJqfTs42E/bBsXlNXB7XcP4J+XFNPJ8sJjeRJWQpuZncQm4lt5HbyR3kTjx0lNyNh4risaHkPpIg90/tnNfG8xaLZKv8RXenaSI/rs30GAOtH3/ozZ30duZu7qzTzoycuZs76akH1+rN6N40+Rvb3FlLUtoB7w+9ubNeK9ff3NmfSp2Rxvvqmzs11d2xI6IXfFNPc/qi22A22OoMZqMVgBmBxRrbIj6ggKtT5IfF2gnB+z8tK54/VUeYOWjlIB4vYigQl5GYu6vD3YELzXvPgPY4/8Ecz18zfH/VB6ATqvt5GMSjB+blqzvWRFVpVKmbM5s8KPs8DLFrldjwm/Lumyp6C7e8mZgO+ydgISS4KqpJ/5Q/GrmpYBV6A/1/QcZ0b8UV7bEpKkRdnqVPxHbAskd/LBCe8AUiJ/QS/Slg+xXum/4f8H9VlqgagM+bj786+UrwW63fdDOHGpOHGnlq+od3o/5nyEdTiE0CiO05UzsqLI59ExOwootG+LW50xxc2YWJ/fjYW5RAXwIhxRQkVg5iUi8dnqAiEWLaFyHGKSpEwEKXjlIkITzExeZfgOUvftn8oC/gv2A0mYEGSuBo2nEftG0aiWpoKYYaTEBEK/JbeCHjvnEfq57xheDDqu0Om91hZwslARYrq+YjsBKbG58yGk0mEIqYidXwoVlIQplcOSCFF85xFwhFW6wiFfBYQYAIhC9SxJXwHB1ArQWxjzYJ2xnCfgIdxpRZBPhLcXML76+0W1pZc+vhgkF0OuYXzE9wa+WZsD9Ex5HhSQS4LKY/Jq3Jr3I8dIgM0k9j/Pcz1ug3C+gXOAbeg5lft6pCwXFYl4aCs6ya9+thFdEALJ8jl+kvYM4XcelZIEtfofKL00+I4BJy/APneLG0fed1FdhGz2me11zXcEZSC1PamixtTZS2Lu/cmyi3MDutyZ3W67AqVG6uWiYqX21JHHmcOUgnD9IMEUkSkYW8hbz3l3fuh5XP5qoUWCIOYspC3n0lxMC4+uXe/YtVL3S92AUG2eYaDlxvXqogvjz1hSl++P6kJdHX/8P2H7cDzlQNJAFWDCQrBhaUS2V7v1z4hcLFJqasOllWneA+y9t3LY4nttcw22uS20Fg4WaX/MagtD7+ZTnx6tZFz0u7Xtn1wrkXz+ESGRbZJ+7QTIWLKWtMljUmyho52rE7nhxaG1PWnixrT5S1SwKXKg/DAneXS87DhaalQ0dumF+aXlQu1dXD6ubUndjbRxID5xM+f2Imkoh+DOxpl6ITfRO6FB4MBhSjnKeC4gIGAUUUgznFxzA4qWxHA7xD2YdBv3IUg3PKKQymlTQGEeXHMDipOqWCoFM1hEHdsGoxf4k49JXil4u/Rt42377MECeTxMkE94E1NlZ4M+qG1xAP3+Pgr2XZ9LUgt9hZPek3ZbLNO64HmNLKZGllorQycziZmFJzstScKDVz0UOvRr5m/lrkpuOW46X5V+aZHZbb/cwOxxtb3+h/a+trw68Pv1b+ejmzo5UpbUuWtiVK2zKl6ZhSfbJUnyjVL5dueV6b2F3HlOqSpbqE+Ingkzi397qKZd8pLnLtVX5njxzg9xSNtS1HlW8dVbWc0PytXA4ww4jGvV7OiPZ8ZESn4h8Z0b8dI7pubSN6SvMIRrLukYzkXBfnjRrJ6/o/kNs+FCN5+7+5kZzr/bC6kbxzVSO5rFu4A7KKkWy01xmMYCcbHStb0s1b3jim/wR/t78s/zewcOmXsNSXESBTug1L30DTcvs4uYrxuojpN+XiU32Z5ujK2uaoNUh/FdmwMrECv2SVsfl+RAGLaSdpisL7XhSbjyiPWfFQJ1gwpMw3+k0EmTYb/R3E3lrLPPqkCP4YOabXMo+OM6UnkqUnEqUnPjKPHs486npz99udieHxxEQwURv6yGZ5sM2yp+WI8q0jqha95i2jHGCGzYK+PpzNMvORzZKKf2Sz/HZsFvvDbvxNbXkES8bxSJZM+Qe2ZNb1uyP3fSiWDPFvbsnkvIVyDUsmZ9uUs2Qqu2NVa1gyTrPdXgfAicBC/z3+ov4OWy87fJNTq5gvb65nvqyzm2YKxtbYTbMGCc6oYdU+zluELeRDfldLK0VEOudNwhYIdG6fy2gwgIHD5uMmKG6NsvkXfONzAcg0h78e3/vid78B379M+34Lvn8F32/D9w58X5srW4dRKg23zrSibAur5tyJHGwe+hY55tDR/Wff+Nlfcv/f+tlf/ezbP7vzs9fmirLIj2SIPSOCv0KOb65liJ1kSl3JUlei1PWRIfZwhlj7ndG3GxJDZIJ6PEHH7uMj2a24A9WmOI1Bn+IyBlcU/bjZ5FGex8CnDGAQVM5hcFE5j8GTyj7cgepX+biNqPGPNqI2YNQdarEq37KqWpyat47JAa7+yFDfR0ZdKv6RUffbMepq1zLqptSPYLzVPZLxlvuU/kaNt9wNrIxNqg/FeNv2b2685ZwXsIbxlrNdxRlvO7tjdeK91izjzWa2WusAmAE4zHV6PTpIczZc7IRo732w27O/q+afP7Ta7tV/XM/8oxMIpF0q+h/QqtNOg6Q5zmbjb1va2Hyr02B2PuqW1LMieAc5qLUsoTamtD1Z2p4obf/IEnrYO3ZPvO1IeM4lasc+Ml0ebLrsbqlRvlWjatFp3jLIAWaYLvhjwZkujdoPelhSzsSX9jO+ytPR2nVyppsPWebM/Po508vMfap6o2XmZZtbGy5T/YHL1GQbauvlzHxCOkNO/rrGi5Iz/9IOIxLMP+28MsP822h7C3J+qArJoinFvCrdNMt+zrJZdl0+OgnGWdpPcerQqWxDb14NBpT6ooy+RhYvprU0rRabwORMNwVLsstb1+TUpD+dhXtiWU+br3r4VHxDRzrF5Rvh4o6J4gw5/vAgcgt/WBeHb+VwecqAydZ46NNr6mV7ll52/P9JL1m135lV+w0ctrVY+mCe+fzr8mvTGc8nl93Ken6Zez55rWeQ179eCzY8w+7mn0/O0UI6z56HmZ3i+bDI+Pt1nkzOMtmlJ5OLV38KOPtOM7k31UHzm7SyDecrT8tXws1nac85C/NZxXxJ+nwW37SR8TZfGi/ZEN/meGl8Mzf+SoVxKMb2CSEhhPv5ELADAqVSCA9iOKWd3xLXLu7MKVCW89T0lpyl2k8feqmWPhaqHuqXKj3nuk8Tk4c/lGemq39rz0xv9Pe4Jifn6jbRkVWXarXdsU10kNDRk4SeprgzysSTgwnqsi84G6COEsG5aV8w6CPrCF/AX0dEfDMzGJn0+WO+kHjO/maidy4qPCyKj7Lhc6c5ktAdEqRMi8JEB89YKZcbt3/FzNVEi5jrJPeIHh6xRtQRJ6/4psNhLsI9W6uPaQkyjEetQaYiXgz6MAorwtgWoo2KRvH9xpyUCOSgUS3047+T68Uyvq25K8ZNwPqrepnkrKs/h5/e01+7eGv+jcHXR5n6zmR9p0BO+/ALzOMoWyN0MSv30dNIxWdm6f/nfxoVbAZW+p60aD6GAC+TtBsnZZl3TVLPB8ds4mBMe8XDQIQiJgP4Lgx8+TXgYZqIzFIUSczNCuzcYYHcY9isqhPvqijxFkoef1NFxd02UXH3MJSwIudea8MtxmO7Cc80RcymOTbDiIXRHKVIOiSu0WPbiV4a06lQlKKJaJgYx2dzuVV7zZ6s52izn7JFX2D6uwjQCZhzEaf/HYLvIbgoxydnL9H+KDr1hi9RNI0eufRlea6XMP/wLM0f91bQESKpy7x3MXoO099HIDkO12xl87iLnFXh1cqq+WuP/oGcPyg8Eo3Qn0NcExDc1VXc87XPoYAfcUzc46+c0zHvS/xFpBZwQse40+m0KJlHFZMRVhGI8P7GW2XpuxdZ2xifEsFvkPXfq7gT3/il5xGmtDZZWpsorc1co/YzpZ5kqSdR6knRcY1vZMpMyTLT9bw1d0AkOm6F1DM7DcmdhnVuHUn0XRULTzC7apO7aq+rJSq/g1Kx/9WqG5uYA/bkATtT4UhWODa8gZJRbKqxS7v2LvQvaKEZu/ct5r1Q92LdfVn+5lb5exy83rh8oPoV3e085oAtecC2oFnaU7F4eOHEwomlwzVfufTyJX76eAefazzLDIwmB0YhyujPJQEePpc8fA6fgj24OHIjwj+B+C7hvEs471T9Te1f176me133tuqnBT8q+GHRj4uYo57EwAhzdCThPc8cPZ/wkcxRMkHNMEdnEhdCzNFQIhxhjkYS0cvM0csMcSVJXElwn5//btRkuXz/Ys2NfqbcmCw3vltuu1tuY8odyXLHu+VNd8ubmPKWZHnLguIFRfbOUym/80RUvtp0Q/FS2yttLxW9UrSQl3q4Gkdbw52WnF2mMabsfLLsfKLsfGqX6eCh+7ICbpcJ4ULzUp3h66e+eup25GbPrZ6XtIvKxZYlnenrZ7969k4lozuR1J2483hS51oswIeSG5Yszm93/UXXm1sZS0vS0vKmL2lpv6G9oX1/+bARnyZuSIEly1FMuaGFAba/AQbYz6vq362y3q2yMlX2ZJV9UbFUpf/K2MtjTJUtWYVPCNfpb9A3W24fuN3/jUN3tnyj5k7jnbnX2t/se1vzHW+ity/RP8L0gsrPJkbHEucnmdHJxJQ/MRNmpsKJWToRucTMXkrUXl5vc2w71/LiUm4vKwXf4+CvZdn0tSC3ObZ60m8O/C5tjp2Cqe57W/Y21cu+V1/UdEL5veNygD+qadzcs1/544Y97p2qn+yQA/6TnUXuQ5qfVCoQr5Ijfsilh8hP96t6qjQ/rZYDnEh/KYDkhv7Xm/gDA6Npiamf9cW0Y/5Tf6Q8/azxL8rJjO2faNpR/JkGAHAqv5R7QODqJW/oVQSwNF/1/lv2dhqZl7YMU2o3nk+dlk/FH+sWV86rUse6xRXNsuvq0c/P58XzVj/Gj9TElau/yCBrQyNzyb+6rPy4ckN82rjqQyuzIK7aEF9h9ksl1uArAu0/dN3m1WTxvGaN4ww3kSWZ3F+UkaVr8G4mt+Twbt243C/lzeenb9askXMbuX3dF89p0+9tkjvSRllBRsrOtJTCjJSytJSijJRdaSnF6fcc5zdl8O1O35rISNmTllKakZK+DbI5IyV9o2NLRkpFWsrWjJR9aSnbSGJ+O7l/fgd5YH4nWTlflqFZaQOMPEhWTWV7GOxanXcKlv8vZ78DYPeavIdzePeQ1Rvo682w/F6nr7ktglJui2AtWdLWHXmErH2QrA3VqO6BNdJtUJaerH+gLAN3X39vhgRpKzdrO6o8Y6vTuJh2oGnqL16+uHU1erQ6rYTUmfKmW+b16pjVqxUZrU47fX5G2tpad6t53yPmJx4x/36YCQ98aFosk6RYHkqLlaQ1Xglzp+1LyvmDcPXYX5bPV61+bcWztu/mD61VY9LxtCxqTos7H+omwOH4ofhhbixW+2Xk0fjeP5STDeQxgMfJEwAfI08CdJGNAJs2MPabyZb1NAJSWj8UKW1kO8AO8hTATrILoJvsBthD9gI8TfYB7Cc9AAfIQYBD5DDAEQ56yTN++avy+Rpo8dlHG1kgbZQ8B3DskeWcjyP0xdUAx0kC4ARpBEiSFMBJjjL1yKVMkz6AfnIG4AUyADBIhgCGOfmzHHyc3A+QJiNklDwT15BzL+aBto6QF+dryUvzdVFrWrnScb/x2viReM2ty5nb2Itpv6Wpv6z5TUdeiesuyugfpx/bSMaEG0FPpN64QsZX2/Il59e4Mp58WhbXkR9LqewB14I+o/yrcf2qG8xpR0aST5Efz7LfVrX+4zLy99JawbeIk04+/cAyfv8DlbG63LR1xuK+1aVk55HLQt+N12W8ryfroEnouaPkJ6InUxxAqc/Q5Sdz+zK7nHjdQ9ToynX1tQPkM9C7z6YqRn4qhUMNqJw66TP0+ukPT69QI8NvUbYCWvtC+vqRVMeK0etXOCq0OZVyUEYXztdzb3Opf7JeeJsLYGlvc7nWHSsrLha2ac/wpxTohpt1buMosVIUFxJ6Oo/qVvIJcTeX2/GWtnTp/85tSLbi1iP9z4irunBTU9WNe48q3IFc0ZmtBpvDajUb7SZH3GaadExQzkm7ZdwIqGXCaDJPTJjMFrPdZ/GZTffCKPa/AVjJ494TTb+HhH9C8A8A7v3gwpfV9/7lh19owNt/MlqNQIMgn9vNRlCAoBBBEYJiBJsQcKdjcocyqlobLS4a+4J7YflAP/0vgN/cx2qaetuNTrtTQBxmEbFziMlgsIqIU0CMIsUqUmxGERGTbGKSXUyym0VElOwUk5xiLqeQy2i2i4hIsQg8RrEso0OgQIVERGiFQ6AAYhYRq4iIPCa7gJhFxCrmsppvqmg517uhuUCALXTjO8aDvkAgfClWjG/jvhAOEk3T/pBvpZR/7Teql3/d9z03dh2+GuieEQG+HmVFzb/3+94PPnVTdu/xv3tZ9Z+waxqy89otRm4M2A1Oi5PPYnSiogxGYw6zjec1WvU2gRd0a4GWOrLe5W3Sm4VXeTvsqVd5Wy2Geen1465W/n3jnpauppYu/kXjEV8wMhea4l82nopkv3D8gi/qCwmvHO9367qhvv38S8cteove1IAaXPOl4/zr9e7hmuamnJVfuIc35FcUZw6sKA6M3lSyCpMDvk5WaTIaVr/l1C5Lu+VUvpFbTqveaKqQbjTdVKbdGXlVvraf5uTk+Cq3nEbwrhvethfuuh10w+fO468OvjL6LRtTdTRZdZSnpX/421OP4UgpGIhQtM4F4qIrJa4JPFNU14Lv0/GHplaKp2L+2TqCpCYDvijFFqTOGV0p6KSoWZ0r4L9IrRQ18e+Y0nmuzFIr+32zswH/hA/Z6i/rLl26pMP3/Ojm6AD/oh6SVbWHI9GVLVO0b3Y61bPQzStFw7rWRl03FdW1d3fcI7qhs06+CNXk6f0dbqSzxa656HSY9se4QlbMPRgnHmoeXNnGSUy1iK98gbunsaOrRd/laVkpHdZ5/FOQ0hHR9VFR+gpMxKB8aqXksm5yXBehIvhiIp2fXBkI+cnjM35v7ZXu7sap8UtNDbNAcPv8oYYoIEYzDMuJ48aGyYnjhoZxBBNAfmAVN3PlkNRF/wSlm6LDc7Osymo0GVa2cHVvpf1UiAxc0XE/BjsH/dQliu6jfFxzIu65KK+dPRxzH39wrM4V8gWuRP0TEZ3HNxVhi7g+gCGAZWCLgbXd4+mFMTCFr1/K6/JPUfTKJl5ZAT/2ckcvq/LQc9TKVr5TIDMMoabAXCQKrNu5Sk+k9BrFd0axxINay6p8YC2zahwrPviFm4mEQ6yWb/wYvhiKwtt0/PGzl8I0ye7CS4CGcTnmE9s0NhHw+YPQKhhKwbkQTEaYUzkxG8DzeOcoVgO9OBaaC7Klk76gP3BlLCW/dAIMGWieH7p4LApjgVVHwnP0BHd3EnTBbuZeqgo5olAPnmPb+Fw0Gg6NXfJHp8dIf8Q3HoDRvYkK0eFAYCwIBBiXbN4kjhq2TKqvMHLGJmDU+6kIu1VKEd56hfXZPTFH01AfqCSUP0WRY/7QGJ7Gi7qYjY419rEK+BZhEVhtuOCom3msmpshKHbrBNdZY9xdZmg0d3hS2eT4mG/WP0ZTj49NCqOHv42pQfIF6grIm8AbwmNcr60cFt/uNa7LvVjrseh6TjkrnV0YEOKLtSKEj6aIcEhPtFyexccAfSGi391PROCqhRYRqDDCxz0ciDeV5yL8rW2QRfhDNxWsioRZntVMUz6SoiNsoagxqGFsr2BTmYJnulra8EVugmnV0wl2lZKIE3QZzmzyhtVn8BPpM3gZvoeVlKXZtnLeHS79HZix1Ly9i1T2y+DXWqPAEo6zedz7dbu5tzffVNBfwXn1jx5m/p7A+duSmr/ts/gZGLwjv3Pode2bla8Vv+l7W/P9GcbRK6Slfbh5nC3JGk8rWwQN4aOpHOkoEdslHvwuKIs/7xydLej/gnXk3C3Q02JlexZnTyfHhYeer+woLhZfUS8atKZW0HopzPIZY4N7+xmrCULNfFNUjsymXpRZU0l3ybljsaNkeC5K/5Ocfxt2eJa/7f80Z/xOwsQyzbsAaGhqNgCl0L+Siw4FW+WCpwC+4/gif/qcPwgXEPeDymppX4gUjufu8+GB45z3Aavh7/1H6Fc4rmnqMn9WHd3HlYkvgbPwv8ac78KnuZrNwq8WjW+t4j0d0IOBP9RsXi44H9CnAdQYUm4DnF8Aq5gMsYoAfGcv4QnfEf4qo4SrjFVNjvsuIhy/uJrRjSkT9PqmN/JMXkJIc5J8nNRZKBLkwwQ4zWpCVBQPqWcVcz62kOZ0ATMRRdJ+bFFAwXUEBbMOqIqfHdlCfjLg3vrHO00UonJxEoJRDE3ys8qA38QqZsCUnfHFwhSuTfCqpT+NQvWYRRm9NAktD+MBbhf8tBGvDoNsVUeJdf/4a+kpEeihgIijgD9b3C3Xbv9l6dbnC94tJe6WEolS4p3zZIL7vENNv+MPMFQwSQUT/Gd/iCkNJ0vDidLwO7OR5Gzsn2Wyx+UuxT/xwXsYNOEr1TC4zwdL23d//swfnFncymyvSm6vWvQlt1dfV6BnBLFUfuDLZ75w5sZWplyXLNfd8CXLDQuKBQUep42p+zAC0fffX9p94L6sUb7Z+B4HrzfiUyQzX5i5sfP2lm+X/UXZN3Z/czdTcSxZcezdiua7Fc1vDr3dx1T0Jit6360YvlsxnBgZS5wff/f89N3z08z5meT5GabiQrLiwrsVkbsVkUQ0lnhinql4MlnxJLRoXxs2CCC0oF3RjUGPwoOt2zeAjQOIXKMcl3AgG4kBpZjBFEoxi0kYvIcBjZkwQAkRTkJEsaBcOjy4UISeGvrbW2/3MwecyQPOxL7H4fOW+vub3qYTfR7m5EDy5ABPfGf4XHJ4MjHFuTMMh5PDYZ6+oFred+BV2ysnbtfc6WAqW5OVrcy+tuS+Nkg4YkgYG5NHmhZKlolDi5deKVnISyH7qhYnX3wSs1dxQIptHFnad0ACVQgskFhe+eLojbbbbYnaY0z58WT58QXFcsXBF4OgIB2Zlw5RH1Terzm4oOScVhKGUf7DHDiXPHBuQbNUYfjW1m8NfvPcm41v0oz1VNJ6ijF2Jo2dTEXn221MRf87niFONdMJP6gmyAyHksMhxhNOesJMBQ7Td6IxKGKOH5HNCuFR5VPYG3PyTsWv+YAbu1382O3ieqoLGbsVg1xkUPEbmWxI4cXgjMKHfGcUfuSYgY7Fs/UUTyDjGUWcT4tjbEgxjzEMUMg8Mj6paNJgpEkDejlU90rwpfAr4YVC6MRF01fsL9tvNLxbe+Ju7Yk3LiYf60n0DyRqTzC1g8naQaZyKFk5xOwbTu4bBjUfPPw11a2Cm0W3ipiD1uRB64J2ef/BVz2veF86+8pZZr8pud+0oF6FtHRoAErbu29R8RXNy5obhe9WN9ytbnij9XX3232J6gamujdZ3csQp5PEaWZvX3Jv34Ji6ZDxhmnxAv4vFC6V6xPcR+jWG41MRX2yoh4GdPm+Lw99YYhfKb3V8vb+77R/vx1Q5qA7CbDcnSx3g7ADVYvjLx1a0NxXyAi6aLHoxjhoBbCEqenNMQEdHE+QszyOuoW5BYImxaRCok0rQhiZVTQrJVqr0qOE/hlUjmDgVZ7Hc8m9ymnk8CtDGMwq5/DIcq/yIp92EWODyksYw0CSdUXZpgIhHaouDNyqftWvMTiDT6qf5R9Yn1BNq95Dop9P82OsQzWDMQwkWQHVExiZV9F5Ei2ad0qNBzuqh9USzasOYCSknkvRLqnbNRCc0vjyJdpE/kWMXM5/MkU7qfVoIRjUhrUS7XFtdwEEvQXnCiTa+QIaI9GCJ1K0+QJ3IU5yhQOFEm2oMICRUGE0RbtY6Magp+jxIokGcEGFXTmhXVS/Gvma5dbRm8duHWMOO5L4Zgek3yl78xCPvb3nnYHhd0ZGkyMTzAiVHKGYgcnkwCSfmJgKJcK0gEfmAfmYvFHBx7neP4eRMcV4ijaheBwjNH8QJk+bU8Qw8oTCpZRojcpOjHQpe1K0XuU4jpIJ5SQGU8oLOASmlI/jgJhSRvhYBGMTyijGMEiVAsMDfx5U3AkGPK1fHB0TKRqpuoSRy6ruPInWkzeGkfN5UynadF4j9nmTulUt0drUZzEyqj6fovnU8xh5Uu3SSLQuTT9GLmjCGHTmj+CoIPNb+fEwrpUYJbig+nlFG1ywFTGYdsurYL42325+c1uivJUpb02Wt75b3nm3vFO6YvdU32hM7NHDh3t3w+lE3wD3WoczjP5M4uwYo4cf1wCjDzDVwWR1MFEdXKo3ff3yVy8L5jZ6h4WS3jDgjH02CbB+Nlk/e0PFSWt7W8Xou5hqd7Lanah2L1fXJXTtb2/lCe9W99+t7k94hhLDZxgPV5hnLOGbZDyTiekA4wkkgo8znseZajpZTSeqaS43vv+guiNZ3fFudc/d6h7ubQ9DTC8noxdknGd6zzPVvmS1L1Hty3rvxVK17kbeUjkhuvUtnFs4t1Sr/1bljaM3ji4brAkbJ8wGwkYZ22jinI+x+RjDeNIwnjCMLxnM3y74i4I75m+UfLPkdsmSwXo77z2NrM52P19WYbhtuj31zYY7V5LmjkQ5fiTBvzRYEtaut/sZw+mk4fS7hqG7BqwtNncYdDvBDE8kyGlmeJox+JMGf8Lg50T/Ri0zWj9IxvfUshrjcum2677nNNdV+P/+cknZfRkYgymwBOkq8V94k612O77loBaM0I+7bKN5su849zRul313mxzw725XNe5RfneX9whElvMKRncrl7fnAaz5HzTe1aHx5imNj3nS+NwWjY+50Hg7mcZdRRpdC2i8S0bj7W0a9xdpvPVK70CANw9pvKtN4+qSRn8TGm/s0Xj3jsZ3YtL49DyNN2hoAsF+BPhaMhqfjKLxmVQan+agDyHAZzlovGNO4wvt6SMIsFk07gjSeNuSxuOzaXTLp9HopnGPmMYHSGhcDNO48qTxNiNtw4VuaZtHZ7daDYQVEIfBYKXxfXG0AwG+EY4+igBvONHHEOCtGBoX1DS+t40+icCFAF+qRjchwHsmdAuCVgRtCHATle5AgG6EdCeCLgTcXnY3gh4EvQhOI0BPf7ofgQfBAIJBBEMIhhGMIPAiOIPgLIJRBOcQjCE4j8CHYBwBPrhLkwgoBJMIphBMI/AjmEFwAUEAQRBBCAF3G2UWweMIaAQRBOgySM+JyuxwmGwOLrSCMi9i2iUElxFcQYCbC/QTCOII5hE8ieBjCK4ieArBxxH8HoKnEfw+gk8g+CSCZxA8i+BTCD6N4BpWIh8LdxqdBgkz0Z/B1M8i+ByC6yk+s8EQ04pYh4QaO+jnkPMPEPxhit1qMNDPI+2PEPwxgs8jWEDwAoIvIPgighcRfAnBnyD4siil224EKYtIewnBywj+HYJXELyKAG8m019BcAPBTQRfRYB3mOlbCL6G4M8RfB3BbQTfQPAXCP4SwTfFInutRqOB/lYqaoLoXyHLtxHcQfAagr9G8O8RvI7gDQT/AcHfIHgTwXcQfBfB9xB8X4abC/0ud/9Adxur6nKPWFg1Qvsgq3a7G03OTiF0A71v2GRqEkLg7na3mlg1QttwTMOHDUDoa3Ya3EDgwoZYfn9vu67LbjKw6g53l93SiaHbbmtm8041nzY7WfWp/n6j9RSE3h4rJKs6ezxQDYTO9lghhv1uncdsBAmdngGHpRdkunUu6M7WmFbEBiRiO4e1Wc2mVh5zIiOPmSTMDJiGx6wCySoknjKbBMkc1i0R2yXMzSdbjVKy3WDkc3O3eDjRHqPRyCMms0FEJIpVQBxCkllkNhuFJKtJRMRcVjGX1SoiNiHJbhAoDgkxGVZ3VP7Hko8cldfJtzFHZc2o8SNH5Y8clT9yVBZS/j/jqLwmb3UO7941eWtyeMvX5D2Sw1vxELz71uStzeEl1uSty+HdT+o25B6t/9ActutJw4fisG18YI1MG5RlJi0PlGXlnGQPbMhhuzLD1di2hqtx5UM5bNtvOR7C1fjgIzpMVz1i/kOPmP8w/CJUf2haTDlsOx9KizXkUbJhSjF/hDwWr4HfkuNfUs7XwlV04mX5fN0ajtt1WTJ0a9WcfCzLcfvkQzlu6+M63oV0vt4vI12P7BjcSDYBbH5kOS2cG3Mr58bcxrkTt5O2NFdtpHQ9cilushVgN9kDsJc8DbCP7Afo4eQPcHCQc2MeIofJEdIb15BnODdmAzp9xw+kHLfJ8+h2TY5zDtckQGoDM8YkOfUAB/XpD0XKao7as5yLNg0wQkYBzpEXAV4iLwO8QsYAPsHBOOnl3NyN5Py8iXxy3ryG47Ypbogbb33sAzhuW8ircctFGf2/Zjj7PiU4+348zbX191Z13H56jSvj95+WxS3kJzbsuG3Ncja2PtCp+hny2Y046Gb04Yk0PWSuJD6V1lK+1VwNyE8/sB7XNlaPeGYZq8tNd+4mVpeyqnO3OcO527KKc/dnoo0pjhzn7s/m9neOc7f5IWqEzt2vk5+DEXA9zQHmuSzn7uw6ZTp3/8GHp9cc5+4PV7biuuaaeR3n7tZUCufcbeOcu21P2gTnbsDSnLv/sDu2S3LuJtK9u02jBK1A7wclglX8uWkVJqA3N52HmBoBOhTR+Qi0CNBBmy5ALNM9my5EWhGCR3DPpotRACqTxlNbeN9sZyzfTTSGo4TVImI2A6twG+FrZpVucySmcVuJLn+UAsRGdIfx5A63b8o/EdO6ff6gLzRFWGPb3b4oRRgNHCPRPOcLEP0d7thmjmwyEMNENefJXBNTcyQHyGi0mmxQJkX6fRFiOKZydxCmWB5A8xCQ/YSF6PK0cASLn0u1chHrMAR+wmVcUUPg9l1eyedDwsRjfsBYrdsfoCLRcIhiNW4/7ZsIULESdzhIhaJEdf8s7Q9Fa6AO4VDMFyt0h9FnkegNzEWgfuFomGiKlXJhi4motrRhRWpixTzFTPTiuSWgDS5qiRUJCJ9fIFtFsjVdbFtsEx8SphBJtFEhrmyM9wZ8V4S8bWZQJ48Qnjl6HISQfqygmC4W2SbIzhdiEaGKgKXXpc0mlD4syB0WSyeqXZ5Dnhoh2Rvb454LRP2zPpIwEQOBKO2DngwTDr2BMLfFtnKJvdOgUsJsthowLYNoMVgsOUSr1QDEgR6BOMsR7TYDlx3G17AJemHY7DAgbr35lZjaaMYXb8YKGwN46Ez/tI++ECtOi8AgyYiaY5syov2ZyZbY5owoJzyDw5rJYeU4StNJ7VQgzKqa/Bf9MTVCGF/q9nBoKuiPafmQMPbH8gXUFCsUMdRbKmJpk9gBLRFQvKIIo6eZG/ON4ctQYxi8RJMvNAH10CDaRDhhoPAIV7t8IULF1BzmjO2AsMsXoWhMn6EmomGaMFoN9H/EK/3nCtz0Fq4SMyfT7Ro28YjvspmTAtcN/Z+QUSteRP0x8Xoyc8VzGGFtk8gWidwaDpCxArfYGgNcaxLOTx6b0gjYhBSzkSuRw00p1JxCHVwxHIozghRBMSITFJkvoFauOT0hikuEkGgycpkQFS5GP9HrI7kcvTjaJcwsYRa4mARMvMr4KF7ZAsbVoCQ9htrR8ASLiFh5BC9wnLiGu2Co+zmiZ5CwuLBqHMJJE6hNItIhIv0iMiwgvUYBOW1EZQLSH/VPXMBqizhh6cQkvnuglSVuj81us8J000/RfioSK+R7wMSrElth49Ci3vBEmL9WW6GY0/4QYYzUxvIQgT7iAn4g9lEkjn6jhJlWNDwmIWYRsYiIVURsMQGxi4hDRJyiRJck22WSMBgdPNZpNkioJYVaU6jNECvg0RA0NlbE43zDY7vTY4b0iDFWnB41xTZlRD2ZyebY5vQoPzLSizKtpMfMGTFLRsy6Upoey5Fky4jZY+ncdn7uSqM4+PkuneLJEOCMlaTHcACXZhAw/9ZsCrJtyyHCXJJRlLM/M+rJFO3JLqyX9gczegiu6uL0mCdWmIra0yOO9GyODD6nOBTwkhdROrwijKV+kzjkhkXSiHGlWMS42UtKkEbgiJn+rzi1/p/c1CoM9H76H9OicGmL2DD939B1XKgi/7MtyrS66PuYqyBVY/o9FP1PSE3XH4j5FSb8OjvB6sroIauL1yT9G+T+75zdieB9rIO6j7oMJh4fws9uXt/0lSAFUbfOCpafqm9u/MpNC/0vXJUGYbIWbIRNHO7RucPjYFmBNcTFB2EeiYVDYEoNGqH3WeWgCS43AGK2Ig4XDC4QYsoSYkoXohg0w9cKUqwRQGBSGLRzumJVgw6DA0hONn/Qh08U+X0x9SBJhWE6Kh2kpnxEBx3GSWnI3+qHbP5xCiYBKJ1HOL3EtosxFJkyUtUceVgIvSyE6Fgf28yH8JMnsRYMhgNRoqvfbsFW9vGGsxWsgcFhMHTAhhkxGVkVgC5EHTHtiJmoNhmMjppY/ojZbNMNGEyxLSNWSSKXaq+J5QGtoyO2Y8TKdx2BmSQuEGZFuVaQC9DaBYJtouAtgGaIA1rJiE2QwxNAgM2KwIbACcBuBODggDlWNBKO+gjeYDPF1CO9urYO4826WEnvaXOj3ug0OAxGvQGr3nva6NIbHUaTwYoEvcvIFnN3fP/f9q49qo3svEszI80gwLKxjfwCAX6ssI2MeOP1S4B4mJdAvGxeFoyEhXl5JGGMJa82IVl2j9Owp0lD2iQladp6e5x00zap06att9m0zjk5JzPKECk6ycnmtJvT09M/cI97sk3Tnt7vjpBGgGxYeze7iWHO77vffc3Mnas7833f/e7t6eksqbFVmWOsrbTGVhtPtVXUdFSXAVtZ0Wlr6zSZO6o7ga0ohbLlNR3niyLpLZUVZVWINVV1nC+JpJtLi3BqsbmzriSS1lFZXghcVWdDeSS9ttK0mrexFoqWS+exdDSWQMXlpXCeEktHHboKc7kpWlNHQwWqCT0sqSZzxWxGq7W5zGgqNxWaKo2FxYXGRhOOK8JxRWXoRsuM6BMiowNuvqi40IRv3mREbyGtDceZog2CKrPV4IjCClM5qqwctdBsRrsV4lA5nKkE4rSJLVkWUbdU1haVN6EEa7sJJRSWmQqNhSYTjiiCiEop56y2DaozVZqk6yhG9ddI9Ucj0MVGpxt0omprLGXF9YiW1BaVnZcmGpTXRPke7ofYA+B8d3tZWZM0Z6GiLkpR5uaaqsKKZvSx29RYXlofpbURVX17Q0VxlK2OqC1WS2lJVbwnFFe319XHH31ZTYfZ9Nq5WU3rlMc1jn56Xd5ZprWjoLywqLQGfWusio3o4y5CWNEQay2KfjRutxbjr8UcQ93Y5JB9DI0z1uKSwsJZ2lpail83ams5prS1IiqkWiulQJrVPuxyuobRIFfomtVYHXZuLKfCBHNdUE93TGAxUYU7PSKuGccYKgsEPgKlAPpUo1AIfeVbOTtrzyk2ogHSyjmKIcI1jkSr+vLZHW1e9N1k6WrNsUw4uJHr6AMxBUVNeLzj6COSaUcFOfjeT5VC1egpOeDFYB+Dnzl+ReS0u4Yd8fcJfovgNwb33wC/BFjBaoHV94L0IoiP7zC0c/8D8CuA/wX4Pyzk4+drKyktLGqWaCmm5cBTtlL0BqBsZaYyQDT8p9gcE27sQTjL2OrqCyxF6EsKhxpKS8qlCR4lFdAFbFMgmKXaPOieYIScdM9qbEjqGM+pLC0uRKfwcA77+KzO5rk+NglfizDmyoZ+BhJQFHr7djQXlBSXl8+md0xyw5dRW+VUoufEaeH6TwAUARTjVgDtRQmESgHKAMoBKgAqcStAlpMQeh7gNLz0yLqOgl+S6OK5MxB3FuAckWyB2afu7ctZ4IRJPHztU64NPMRehxK1ADGvXcllZxQAuyOB8w43DjABMAkwBXAVABQ9HJyO8wB4AaYBrgHMAFwHmAW4AeAD8APcBHgBIADwIgBsCsx9BKAOoB6gAeA8QCNAE0AzQAtAK4AVoA2gHcAG0AHQCdAF0A3QAwBuzdxFgF4AWBKd6wcYABgEuARgBxgCAEc6jgWAHWI4J8AIwDzAywCvAHwCekFWzIcwB5wILS01BTInQu53ICM4EXKfTNo1ntyNkHsVTgOeg9yniC10iG9CsU/HOsTvQegzcFd71vn4bezixy3ipgP2sxD6fQBw2OP+AEKfQ5B/CLvmcZ/HwwyEvoB7AoTwUrt/iB89hJbwIAShRIc87ouQ8CUA7Nv+RxD6MgBe//ePMQuhP8F9AkJ/CqFErzvudqyXx5zuIqTXxW7oeVe+xvOOew0K/hkAaJG5OwBfAfgqwJ8DbKRHxb+5RytTvwZZ/gLgLwFgg0bu6zDEMuOTaPCbHLNHyPHxKYDxCDWE/iKq8XHMAHLfgAJ/DXAXAD/UmCce9zcAfwvwLQDse0e4x7m/A+7vAf4B4B7AGwDY3+4WADjdcd+G0JsA3wHATnfliq073SX43n1kFWBUcBtSJd8723rfO7uDx8ey07U8Oi44J0TnBC8duZPC9ilx+xS/fWr5qke8euMXqE5lFXiaAXkApAa8jYCsSOTp+d7VY9+7+me+dx8+3ztwq0MNZJpKkyNqj4NX0x5iXGRiDnpdB+UIjdZ98CHGRTKW6YJGjpDpouYhRpRJf/hz4Ltj7EqVI8qU0536ECO6zpwjX05HCSem0+SIMuVeg2tCiBtJqsmbJkeoaRoyIUQ1PfMs/FB7Fh7IXSpdPPNeuhg+80v7MPmloSeW605bOnAbGhyF+OKae5PRYPcw77gqhRF6pIdQQ4wQsTgXMYndzgkLGYurIzuhIbvJi0B6STu0WS/pghyj5CSQq5IbaK/kBgoEfmHkDHBAYnXNkvXgDXqeagbSQnWAq2cL1QdN2U8NUbhhsRtoi+QGCuQBFLgCHJBYXeOUD5iblFsVi/OqGqEVm9UX1LG4XvU4MJPq6XjcjLoBNyk9xMTiWOYaMNeZF+Jx5pROaNnulKmUWByX0goDd5tmUBOLs2vcwHg1vnjcTU0LjN3WVDyES3E9qePATKZ643HXUluAWNOwO6gUhxDG1/Uuhjo+q0HIahCzGkJZLcGsFiHLKmZZ17sYtvO2LsHYxXf3CcY+vv+SYLzE28cF47hgmBANE7xh4kldDOvuk4KhSTQ0hQztQUP7sq1rufuiYOsVbdh7zoa952zDsIOAbZQfmxJsU/xVr2DzCoZp0TDNG6af+Rq+j76Gg/q4ryEKr/oa9lOI+aleM1hC/vSECmGCmwlMecRuJrCt0mc+pE4mKQrs5KHqL/WTLOWnPLJt40ZjLg6silWvcyygk+Rl2JR1eTWbr/fzqsSNE5OUTGXTHumEoPbINnVj02WT8emElG2yFCYhRStLSUlI2Z7g0pAZT/GnJuTbkeDGIE/JSHBjkKfslG8al5CyK8GlQZ6yO8GlQZ4id77Ywer8Gewe/052r38Xu8+/O6FlY7tps/vZA+ucEDI3zjuiYLPWTajXJc2bvS7vHla/iWfNsDmPnZ5Or9v7Wl5XbCtHNpfNe+zk+81c0cHHXtGhTdZ1mD3y2LqkFar3JtQQ28hvzaTUffJzsoaNN4L07dt480dPnuwMscmpbP6do1uYNr4/4a5lG9uNxvrmI6ezHnjC8llPWD4bj4RPqxXjLgzHttSKevY4WzBC+HNYo0+PxtATnyf9uehXVPglpT9v49+YL2/diutJrpw1zSVMPGeLtjT5/pDvoA/3b/9h33622HfAp/CRrI4tYUvZMrYchXRsBVv5uXT/Efakj0KjOoH453172VOwrjp79nO0/zn2nN/Amv35nhOye4m5KvgMsDL7nao107JlU3Xjf2t+AUfZat/RacWCkjuO3m9H2RrZKHgs6uiIQnFHR/mz9h1LvFf523gaT9ZcUE58QT6VnLU8qjz+/dZitTOJw3UbTgWvT/KcGubgDs5veip4wurkbKPv+IZTpctleZrY5k1NBX/EPbItsvuT7hWfl2197NmtT/nsG59RPjV8w4n9j6p/g0nLX2Db0FNplxkWbAnTs2/hfidP75CFH9sffcfW9Dpigbr1g4R263xf2u1kvPQm2u2R41l0srfqVnnCZO+uhMnep+IpeLJ3AZ7sXXCzIDrZG4Vkk727k072Lk6Y7P3rnL/9FI2kXB0Jxh2AD5yRVGefcpk2MIphy/gaKym2GmGLKLZ0YiMntm+CGTM/XWZF3ciAGreTYhMpto7GDaMfQzCrlhYejtDeiSsTk9cmJDMotnuCOTKflgyc2GaJDZxxgym2kGLD5Qb2Sa4Z2v48wAfEFJms2XPgGjewRXJNkLCR2THR2BjRRFfVtXvs2PCI3STy9ZuxPr5f5kbJ0hg3MhrXGhmxVRHb6d4zq+KmzYVgKeQ6oPG3birEvS5uLzQqtmovlDrMR1fhB9CVDGowE/6XWpGSdksTYvYEmT08s2f5Qj+Pj+UB+/KQQxhwigNOXjr2jgjMZZG5zDOwcqfocodc14Ou64Lrhui6wbturBD9oGvZf3BFcUG548gDjAvVkt7+t8MY9sxc9MxclNRc9NZzx8L5J8LHS8OGY+FjxvCps+Hi0+H8wnDJ+bCpIvz8mXBZZfj5hpX923L2rSgQLFIrOQpTnfLufr6wFh3h0upw+blwwYlwkTlcaAuXPL+iZXLzVhQIFumVDIW+Xrllnbiw3wj7vBaFjYWv777juk3eJsFIDxEmYBD7zjs/OXhkyf3Fii9XfMW9dHbpbNhQ8JrqbaxJX7Z18auabbxen10w2nk0chgdvJMTjJxgcIsGN29wP32VOv8UVOrLUZV6j2jt4S/0CVZsD7Be4u0OweoQDE7R4OQNzqhu/evFr7u/VvFXFYLhlGg4xRtORZXsJ9YpxGNtqrtz5e5xEd2RSjS2bNy64YNHvnJw6eTSyddYNB7nF7wnF/mjrMPvXk0O68S9kdV8oitP8f10pjWT+P5uJYQzqdYDqu/vqzEiRkzZ1ZFNiFmQIGZTHYdUYp75DGJ+mKfpKid/WKRCOCwXUmLrNH1j24daga7E27ne8RMs5Sc/EAp06iko0FVJFejqpAp0OqkCnUmqQE9JUKBrkirQU5Mq0NOSKtDTkyrQtyVVoGuTKtC3szr/DnaPP4Pd69/J7vPv2oICPYmyfUMFenJl+3oFenJlu369sj1p3px1efcmzZu7wapDm8+7P2nevA1WHUqW9+D6VYfYQ5tS2x9+aoaEI+xzT8WQYHjsFeVvsq5NbATLYrWcP3tThoQE0wxbkEQFrt+SIcF455Fbw65bx+nJFPm5T1g+7wnLH0RvhENPrRXjhoTCLbXiYdbEFo0Q/iNsse8wepeUfJ70P4d+RaVfUvoNSQwJhnUrASW5crZsjSGhfEuGhKO+fN9R3CePuRRsxZO19+8q2Ur2JGzg+sT1nMKr+Jz2EQjPsDq8EWwBwnOsGa8VpMPbwT7pWWrY07BiEF7LJ3FDV6i/CWMzuwfhfljrh7X6SLYNr+JzHLVWuy87ySavFxH2bmLE6GP7H7P+zsBTqWWDNYZYJ2znyl5+5Bo/U3gbVitexaeAdfuNrMd/Iom5yOg77iu4430X5qJCdtpXGDMXFbLXZO98U0w9b0piLjJt2Vw086jyeJS+jlWDBA7PbmguupHk1+ibgzvwb9pcVJRwZTd9RY812LzABrZseFhzj+yLsvuT7rUovoLOI8/+0ad89o3PuDVzkelRo2/UXDSHnsrHZMrfj68zFyWmvyQLP7Y/+kzrzEXqW+cT2m3+fWm3p28uUt/6aoK56OUEc5ExnjKaHQvFttE9hFX0HrMsV26spsK15wNTk239ZrLF2ARVfLM4aoJCIZkJ6pWW2cyNTFAfHPvTjyD0bwAgbHN7AMoBfksMU9wEO77RBm9wtb9O970I0Wn7TXHc+wAaxpI8dncSw9jsgTVOeqh8Uke9dbv2QebofnxrnPYukEmyS1vtSWa1gx9Qs9otgE8AtAC0AmBTW4lkaotb2d5b3z2uBZ5aK4AVoA2gHcAGsGWXvadkiCtRvDvHPambvrkKZahWd5NmQ3Nc10UeH8u9A8uDQ0LvsNg7zEvHXlZgHCLj4Bnw5xOdUyHndNA5LThnROcM75xZIVpXzXEN2BzXIJnjnvmmPfNNe2Zs/E03Nj7zTfsQ+qYd9KYtnXo9A8WgEF9ae18bDV5w8CNuKYxwWnLBrpV+K1LcFand3UQdGYtrILuhIS+QfUD6yWFos37UrChtDDUr5EcS5AOIvC6lXQfuAjkLHJBYXT7yPDilNVGtQKxUF3icWakBaMpBigXipK6AN5qVGpPSxoBrosaBAxKra5K6Ccw5lVcVi7umaoZWbFX3qmNx/epJYK6qZ+Jxs+pGaNJmmmVicU7mOjA3GHNKLK46pRuYCylcPM6T0gYDt01j18TihjVeYK5pbsbjzqVaYexuT+1JjcVdTJ0E5mrqtXjc9VQrkPY0T1osDuG780370NjhG+9XS+NZyNAVNIBfG987IHQPit3YAt89zLMjQvcI75oQuif4KY/Q7eG914Xu64JhVjTM8obZjTbhW45uwtcndmDjdscl3s4KHSzvcAkdLsEwKhpGecPo+2yHfw8ucgM7vE7U5onaIrDB6+OAcn1Ks1j06rZPbVuI/m/FZA+bt72RZTvSt1exTDGd6cRymhLC6VTnTtXyjhojYiKKXRd3E5FdkBDZTV3cr4rsNZ9BzI/3Gvr3kD+hUgB3qhDmvwgbV19xc/qY7IDFBiwYlCpX5RMsx2BpA2/grXF7h6a4SdisOkIOuUsiGcOTE8NejnNMeIxOr8fLOdycChQKN7HEoIBFRNyTU5GdzZOsd8zRMumpnfROsBaYjCiJKDkAh6BycsThiVAexwxCdJIZSXrBm5XTwLtQ3SCt4I917hrADCRug63HJ13s4Pgk64DtsmdmItSYa8KBJZ8I6XVz0YU9UAjvVk6MoFN4kQiJJacIYbdHlEPS7ubK4YhyBEtfEeVlvMV8RDnKncL8WETltV/xFkVUdlTWE1GyEaUzwji9Y2P2EcSTnHckQkx4sFQXITgO1XwR0RlImY2Q455hLOFF0oYvO4avDE56PVNeD3cc7mQpmZhVv0lZ61dKaWPxMcewRxImM/HdT12b4f4dnsjbABGA/wBYBvgXgJ8D/Aweldra2W5tskTIdktNRNVd39Bhiajq2i2Wloj6gqWpqbU7QlU1dVoi6tZ2c0sdSqxqMlc3RlSWno52M5cL13EAIDsm9M7FhE+8hIwNP028HfsVb4RwTXJ5EF0MUAlgBZgF+DjASwDzAC8DvALwItShmoE/aamUj8bEL6xAwIoAEMl+yZwax93uDPcqCRpB9H58KUOhQL8ppTKsGghQK1SqMi9MWfhfxxGm9vCrR5jaFjgP/29Rp/nEI0wZ+MQjTOXy6453wvS+FQWpzItDmEoJWHhNgUAZRcrIU8YwlR6ommvgt50VqHMidY6nzsWicgQqV5TVt0KjGmAAYijl9jChDRRI/2iYJSAiNZA3l8+n5QhErkjk8kSuLA/KhUZfRUqAmEvhNRZBUSsqanlF7QpFKU+FNZnzhlvHed0FQXNRhGMwUBOmmEDNfNaCW6D2i9T+EJUbpHKXnhOooyJ1lMcHusHtaIxUnopD9AZPCtTzIvU8v+6IDqDKU0CRKJ4+T833LxYLjF5k9CHmUJA5JDBHROZIiDEFGZPAFItMcYBGWbdnBLatEJQyLZyye37PrQN8Zo+QckGEYyCU4gqmuISUK2LKlUBVeDv6vlOqDmGYp8JMZojJCjJZi0icPygyB3l8oKtQHXrnLUVqwBPwoKt5i1IHSDhBepjeGZiZ8/G72gS6XYSjO0QPBekhgWZFmkUn2Aa3rdJhmCfCTOonNa9oFope3nZr2zz6h6p1qOo0dHPwynhLlRHomutH3y67qi3KRII+4NQ1FuVDiQSIsIoOUGGNdv7wgurl47eOryhSlToM6Lz0cwjUOwPOuXF+V6V0COqTovpkwBxW71vYif7bX9V9Sser96EDIssAMgNOUZ25wC0eFNTZojob4lJkCZ7FGkGdK6pzk2U+gCBdy2uK0LGQG6VXJbpoBogyS6YojfK3o/ztKB9AvzHmpcaPNC6oBCpTpDJ5fITTM+Y7F0pf7rvVt6LYptyHAeWljz3qhs8C4ETUmLu7CDmidqW7QYpFKLurq/K72mTRqqfShPsR7NiJfujoWLBLdNEEAMzSDgCzFH0bmNtR5nVllEb5u1H+bpQP1K+2KCNQe0VqL4+PMHTnhH6kUu58AAD9KH3uJpBdgek5kDkzuwk5ogZgeqABEEI2XWBapHWLSvQ7pfUirQ9UIUmKqafwZ10V+r/6esZr9XfqX0u/A4oXlCLhvep71feJN+rerJP4+7b7Nr7N9t3u73VLEXzXBTgu9gld/WJXv7wsyJlEIxEnTdJiUk2ra0q1AWknOuFqm4guuNwmSetRT+CnB2RNjX3EIBEnlySpOkqGpXVILhNjUMclYhzqAPIACkwA1ydtWS+v8aokhUeJl7gmIzOrQjlWo3iJm1hpgwgobYgXsNIGkTU1NpBNZJw0S9J7lFjJdiA2sguEyGYkfD6UCOxbT/YAB2RNjf3kJTJO7EhIjROWdABxkiNQh528DHUAwSKrSxJZXWtrHJOWXYmSKZKTEbekMfBKS7JMSUuyTElLsoxJS7KMSUuyyGtEiHoaRb90/iPn57kXW+ZaAi0vtkidOHX7fOnC7pdP3ToF79CdGALV0U4MPbGTuu2+7UaCSdHr9rsECASv+e9Av0YpEt5133XfK0L/dtQfK96s+Kb/Wwnp99333aC0QkcXEkAuCLaLou3id33f88lzrYBirY2Ik3aiQ0Y6pQ7XQ/TCE24n+uAJA4HlZIh+4ICsqXGIcBBx4iQuy4gLdT9EJqTlz5wEXv8MyAMo4AFuSOp58hqvSf3uWrz7xclN4hw0vZmsgedxg7DA8wDyAArUAgdkTY295AAZJ4OkXUaGSBaIQ+ozg1KfAYIX5BmVFuQZXVvjpNRZJlf7jFdGpiWtyA3yBajDTZ4D9QaQB1DADByQNTXWUHUyUk+dl5FGqhk/PKoN6gD91UOJPIACNuCAyGtc1xsDLegjRM2gl3PiuyobA3pXpZ5AnwIa3fyRWwX8ngrpEDSVoqZyXhnWlAPgRFT/3ouEHNFVpPbCw0QI2fbNHxE1+xZNi8OCJk/U5G2haK2sfJG8fLosoWSJEjSHRc3hZJn1CHbr+IxqdCzmRulVBEvALLUhuK2Uom8D83qUQe8oTO9G+btR/l6Un2fCTNonU19JXagXmCyRyeLx8VZKakAdzshfOCpm5PNHm3hbN5/RI2T0iBk9oYzBYMYgf2lEyLgsZlwOZUwFM8DrgJ+eETKuixnXA9owo5/XoM9HPufkvV08UyswtSJTG2Kag0zz/RGB6RKZrhAzEGQG+MFhnnUKzIjIjARU8XKld2t4xiwwZpExh5j6IFN/XycwbSLTFmIuBBn0hkJF7QIzJDJDqBy9DckpBKnMDGuPzM+K2iP8c9X3D/HaVkHbKmpbQ9quoLaL7x4QtIOidjCkdQS1Dt7pErSjonaUvzImasdDWm9Qi24Cr52ovSlqb+JvxRVCCbXuBgZ/Oobp7MCsSGfz+nP3PDzdJNBNIt0Uom1B2sZ39Ap0n0j3hWg2SIOKhB8dE+hxkR5HvTRWsPIexdMWgbaItCVENwXppvvdAt0p0p0huj9I9/MDQ/ywQ6CdIu2EcmkAmfIazt5jebpRoBtFujFEtwfpdt52UaB7Rbo3RA8HadBH8ZevCPSYSI+FaE+QBn0UP+sTaL9I+6GqLD67dHFUzC7lywZ55yiffWV1DUkumM3x7lkh+4aYDUti6mvw0pBY/2ohGoCcJyTTRjNe/rEZf580S8Ow9LESHXcnJTIE2aLcFNEjjVX4bddDsDCkAHkokV8AuUL+p0TwO80tZfFIWTxSFp+UxQdZ/NLgU0XVUDinhXooEbgUCwV9Y9e76xtIWNm+Y14V3oFVT3sxzJvD23cvXH2VWVAtoJR98+pw6o4F2yun50+HdcaFWVFn5E808u1dvK5b0HWLuu6QbiCoQx3WKehGRN1ISDce1I3zE1cFHSfqUFt7RJ03pPMHdZK5IWZgQpe/pw7aDuEC9ZPtmYvUq2kL6gV1OH3ngvuV/vn+FUK143BYX7Y4K+rL+HIb/C70g4J+UNQPhvTOoN7Jj0wI+klRPxnSe4N61MGvC3qUGXVzn6j3o6bMqYXHmxM1Z8W+7MDw1grnRrhI/WRP9hL12bRF9aL6nbAuZ0VB7DgcB2ySlGVZ/ceypQplwDKyYk+27CbeWf/TemtfPmpZOLQ7V49dsfDKbo0GPQUEAfVKpkKpkSTnM4LirKg4yyvOgtDtR91BhowCCW9kmNoeUD4O0hEwOjTqqTNQCWYXjEYAKeh0IH9SUgilquD7W7Wi1tFlqGcVKpW1SpC0Y6gmlLvg/FFA7ygQIPGHUxxIFZIsGQ0WpJXbAunwH1Zk8onHCqGFamKQR4AkFgMmV7ljRRGDeqVCqQ6oXqTnaFQvNaQEOVWGtWS20riiiMGZRPac8jHJZRCMAadsUSrRA5HhAKGgPcdQ2xAdOFKGo4QdMzKsJW2YkeEsgQT4APWiek4dwP/uTysUijkzYaYVb9CF5pPkG5VKwDNUFan4RzITliw7UVJ9SPHtQ6rqM+S381OrK8lvV0L4zRKz0lKm+E4ZYTlJ/pPCrKwjFP9MEHVqMnLKnNGnVfxYS/XtJn+2u+qEM13xryrzAUee4u1cJWLezlM5TpNvP5fmqCDfLlZBTAWOOa1F4Z+nU86d5P8DasIbtQ=="))))